#!/usr/bin/env python
#
# Beacon transmit
# Options:
# - center frequency
# - start time
		next_time = sampler_util.find_next(self.args.start_time, per=self.args.rep)
		print "Starting at ",next_time

		tt = time.time()
		while tt-math.floor(tt) < 0.3 or tt-math.floor(tt) > 0.5:
			tt = time.time()
			time.sleep(0.01)

		sink.set_time_unknown_pps(uhd.time_spec(math.ceil(tt)+1.0))
		sink.set_start_time(uhd.time_spec(next_time + self.args.clockoffset/1e6))

		sink.set_samp_rate(self.args.sample_rate)
		sink.set_center_freq(self.args.center_freq, 0)
		print "Actual center freq %1.8f Hz"%(sink.get_center_freq(0))
		print "===> self.args.gain: %s"%(self.args.gain)
		sink.set_gain(self.args.gain, 0)
		sink.set_antenna(self.args.txport, 0)
		#code_source = gr.file_source(gr.sizeof_gr_complex*1, self.args.codefile, True)
		code_vector = numpy.fromfile(self.args.codefile,dtype=numpy.complex64)
		code_source = blocks.vector_source_c(code_vector.tolist(), True)
		#multiply = gr.multiply_const_vcc((0.5, ))
		print "===> self.args.amplitude: %s"%(self.args.amplitude)
		multiply = blocks.multiply_const_vcc((self.args.amplitude, ))

		tb.connect(code_source, multiply, sink)
		#        tb.connect((async_src, msg), (sink_queue, 0))
		tb.start()
		self.print_info(sink.get_usrp_info(0))
		print "Starting"
		print "Restart time: "+str(self.args.restart_time)
		while(True):
			print("Cae0")
			tnow = time.time()
			if (tnow - tstart_tx) > self.args.restart_time:
				tb.stop()
				exit(0)
			print (sink.get_mboard_sensor("ref_locked"))
			print("Cae1")
			if self.args.clocksource == "gpsdo":
				txlog.write("%s %s\n"%(sampler_util.time_stamp(),sink.get_mboard_sensor("gps_locked")))
			print("Cae2")

			# print('Sensors names:\n')
			# print(sink.get_mboard_sensor_names())
			# print('\n')
			txlog.write("%s %s\n"%(sampler_util.time_stamp(),sink.get_mboard_sensor("ref_locked")))
			#txlog.write("%s %1.2f\n"%(sampler_util.time_stamp(),sink.get_time_now().get_real_secs()))
			txlog.write("%s\n"%(sampler_util.time_stamp()))
			print("Cae3")
			# if async_msgq.count(): The whole block was commented by Alejandro
			# 	print("Have no sense \n")
			# 	md = async_src.msg_to_async_metadata_t(async_msgq.delete_head())
			# 	txlog.write("%s async Channel: %i Time: %f Event: %i" % (sampler_util.time_stamp(),md.channel, md.time_spec.get_real_secs(), md.event_code))
			print("Cae4")
			txlog.flush()
			time.sleep(10.0)
			print("Cae5")


if __name__ == '__main__':
	#parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser = ArgumentParser(prog="HF Transmitter", description="Configurable Transmitter\n")
	parser.add_argument("-a", "--address", dest="ip", type=str,action="store", default="192.168.10.2",
	help='Device address (ip number).')

	parser.add_argument("-r", "--samplerate", dest="sample_rate", type=int,action="store", default=1000000,
					  help="Sample rate (Hz).")

	parser.add_argument("-t", "--rep", dest="rep", type=int,action="store",default=1,
					  help="Repetition time (s)")

	parser.add_argument("-s", "--starttime", dest="start_time", type=int, action="store",
					  help="Start time (s)")

	parser.add_argument("-x", "--txport", dest="txport", type=str, action="store", default="TX/RX",
					  help="TX port")
	parser.add_argument("-g", "--gain", dest="gain", type=float, action="store", default=0.0,
					  help="Transmit gain (default 0.0 dB)")

	parser.add_argument("-c", "--centerfreq",dest="center_freq", action="store", type=float, default=3.6e6,
					  help="Center frequency (default 1.9e6)")

	parser.add_argument("-f", "--codefile",dest="codefile", action="store", type=str,
					  help="Transmit code file.")
	parser.add_argument("-b", "--clocksource",dest="clocksource", action="store", type=str, default="external",
					  help="Clock source (default gpsdo).")
	parser.add_argument("-o", "--clockoffset",dest="clockoffset", action="store", type=float, default=0.0,
					  help="Clock offset in microseconds (default 0.0 us).")
	parser.add_argument("-z", "--restart",dest="restart_time", action="store", type=float, default=3600.0,
					  help="Restart every n seconds, to realign clock (default 3600 s).")
	parser.add_argument("-p", "--amplitude", dest="amplitude", type=float, action="store", default=0.5,
					  help="Amplitude factor [0,1] (default 0.25)")

	args = parser.parse_args()

	#self.args.ip = "192.168.10.2"
	#args.recv_buff_size = 100000
	#args.send_buff_size = 100000

	if args.start_time == None:
		args.start_time = math.ceil(time.time())

	if args.codefile == None:
		args.codefile = "code-000000.bin"
	tx = beacon_transmit(args)
	tx.start()
