def run(self, starttime=None, endtime=None, duration=None, period=10):
      op = self.op

      # window in seconds that we allow for setup time so that we don't
      # issue a start command that's in the past when the flowgraph starts
      SETUP_TIME = 10

      # print current time and NTP status
      if op.verbose and sys.platform.startswith('linux'):
          try:
              call(('timedatectl', 'status'))
          except OSError:
              # no timedatectl command, ignore
              pass

      # parse time arguments
      st = drf.util.parse_identifier_to_time(starttime)
      if st is not None:
          # find next suitable start time by cycle repeat period
          now = datetime.utcnow()
          now = now.replace(tzinfo=pytz.utc)
          soon = now + timedelta(seconds=SETUP_TIME)
          diff = max(soon - st, timedelta(0)).total_seconds()
          periods_until_next = (diff - 1) // period + 1
          st = st + timedelta(seconds=periods_until_next * period)

          if op.verbose:
              ststr = st.strftime('%a %b %d %H:%M:%S %Y')
              stts = (st - drf.util.epoch).total_seconds()
              print('Start time: {0} ({1})'.format(ststr, stts))

      et = drf.util.parse_identifier_to_time(endtime, ref_datetime=st)
      if et is not None:
          if op.verbose:
              etstr = et.strftime('%a %b %d %H:%M:%S %Y')
              etts = (et - drf.util.epoch).total_seconds()
              print('End time: {0} ({1})'.format(etstr, etts))

          if ((et < (pytz.utc.localize(datetime.utcnow())
                     + timedelta(seconds=SETUP_TIME)))
             or (st is not None and et <= st)):
              raise ValueError('End time is before launch time!')

      if op.realtime:
          r = gr.enable_realtime_scheduling()

          if op.verbose:
              if r == gr.RT_OK:
                  print('Realtime scheduling enabled')
              else:
                  print('Note: failed to enable realtime scheduling')

      # wait for the start time if it is not past
      while (st is not None) and (
          (st - pytz.utc.localize(datetime.utcnow())) >
              timedelta(seconds=SETUP_TIME)
      ):
          ttl = int((
              st - pytz.utc.localize(datetime.utcnow())
          ).total_seconds())
          if (ttl % 10) == 0:
              print('Standby {0} s remaining...'.format(ttl))
              sys.stdout.flush()
          time.sleep(1)

      # get UHD USRP source
      u = self._usrp_setup()

      # set device time
      tt = time.time()
      if op.sync:
          # wait until time 0.2 to 0.5 past full second, then latch
          # we have to trust NTP to be 0.2 s accurate
          while tt - math.floor(tt) < 0.2 or tt - math.floor(tt) > 0.3:
              time.sleep(0.01)
              tt = time.time()
          if op.verbose:
              print('Latching at ' + str(tt))
          # waits for the next pps to happen
          # (at time math.ceil(tt))
          # then sets the time for the subsequent pps
          # (at time math.ceil(tt) + 1.0)
          u.set_time_unknown_pps(uhd.time_spec(math.ceil(tt) + 1.0))
          # wait for time registers to be in known state
          time.sleep(math.ceil(tt) - tt + 1.0)
      else:
          u.set_time_now(uhd.time_spec(tt), uhd.ALL_MBOARDS)
          # wait for time registers to be in known state
          time.sleep(1)

      # set launch time
      # (at least 1 second out so USRP start time can be set properly and
      #  there is time to set up flowgraph)
      if st is not None:
          lt = st
      else:
          now = pytz.utc.localize(datetime.utcnow())
          # launch on integer second by default for convenience  (ceil + 1)
          lt = now.replace(microsecond=0) + timedelta(seconds=2)
      ltts = (lt - drf.util.epoch).total_seconds()
      # adjust launch time forward so it falls on an exact sample since epoch
      lt_samples = np.ceil(ltts * op.samplerate)
      ltts = lt_samples / op.samplerate
      lt = drf.util.sample_to_datetime(lt_samples, op.samplerate)
      if op.verbose:
          ltstr = lt.strftime('%a %b %d %H:%M:%S.%f %Y')
          print('Launch time: {0} ({1})'.format(ltstr, repr(ltts)))
      # command launch time
      ct_td = lt - drf.util.epoch
      ct_secs = ct_td.total_seconds() // 1.0
      ct_frac = ct_td.microseconds / 1000000.0
      u.set_start_time(
          uhd.time_spec(ct_secs) + uhd.time_spec(ct_frac)
      )

      # populate flowgraph one channel at a time
      fg = gr.top_block()
      for k in range(op.nchs):
          mult_k = op.amplitudes[k]*np.exp(1j*op.phases[k])
          if op.waveform is not None:
              waveform_k = mult_k*op.waveform
              src_k = blocks.vector_source_c(
                  waveform_k.tolist(), repeat=True,
              )
          else:
              src_k = analog.sig_source_c(
                  0, analog.GR_CONST_WAVE, 0, 0, mult_k,
              )
          fg.connect(src_k, (u, k))

      # start the flowgraph once we are near the launch time
      # (start too soon and device buffers might not yet be flushed)
      # (start too late and device might not be able to start in time)
      while ((lt - pytz.utc.localize(datetime.utcnow()))
              > timedelta(seconds=1.2)):
          time.sleep(0.1)
      fg.start()

      # wait until end time or until flowgraph stops
      if et is None and duration is not None:
          et = lt + timedelta(seconds=duration)
      try:
          if et is None:
              fg.wait()
          else:
              # sleep until end time nears
              while(pytz.utc.localize(datetime.utcnow()) <
                      et - timedelta(seconds=2)):
                  time.sleep(1)
              else:
                  # issue stream stop command at end time
                  ct_td = et - drf.util.epoch
                  ct_secs = ct_td.total_seconds() // 1.0
                  ct_frac = ct_td.microseconds / 1000000.0
                  u.set_command_time(
                      (uhd.time_spec(ct_secs) + uhd.time_spec(ct_frac)),
                      uhd.ALL_MBOARDS,
                  )
                  stop_enum = uhd.stream_cmd.STREAM_MODE_STOP_CONTINUOUS
                  u.issue_stream_cmd(uhd.stream_cmd(stop_enum))
                  u.clear_command_time(uhd.ALL_MBOARDS)
                  # sleep until after end time
                  time.sleep(2)
      except KeyboardInterrupt:
          # catch keyboard interrupt and simply exit
          pass
      fg.stop()
      # need to wait for the flowgraph to clean up, otherwise it won't exit
      fg.wait()
      print('done')
      sys.stdout.flush()
