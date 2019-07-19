#!/usr/bin/env python
from fractions import Fraction
from gnuradio import analog, blocks, gr, uhd
from argparse import ArgumentParser
import math, time, calendar
import datetime
import sys
import time
import numpy
import sampler_util
today = datetime.datetime.now()
delay = datetime.timedelta(days=1)
HOY= today.strftime("%Y%m%d") #formato


class meteor_transmit:
    def __init__(self,op):
        self.args = args

    def print_info(self,uinfo):
        print "mboard id %s"%uinfo.get("mboard_id")
        print "mboard serial %s"%uinfo.get("mboard_serial")
        print "tx db name %s"%uinfo.get("tx_subdev_name")

    def start(self):
        txlog = file("hftx.log","w")
        tb = gr.top_block()
        r = gr.enable_realtime_scheduling()
        if r == gr.RT_OK:
            print('Realtime scheduling enabled')
        else:
            print('Note: failed to enable realtime scheduling')

        tstart_tx = time.time()
        tnow = time.time()

        dev_str = "addr=%s,send_buff_size=10000000"%(self.args.ip)
        u = uhd.usrp_sink(
            device_addr=dev_str,
            stream_args=uhd.stream_args(
                cpu_format='fc32',
                #otw_format='sc16',
                channels=range(1),
            ),
        )
        self.print_info(u.get_usrp_info(0))

        u.set_clock_source(self.args.clocksource, 0)
        u.set_time_source(self.args.clocksource, 0)

        next_time = sampler_util.find_next(self.args.start_time, per=self.args.rep)
        print ("Starting at ",next_time)
        tt = time.time()
        while tt-math.floor(tt) < 0.3 or tt-math.floor(tt) > 0.5:
            tt = time.time()
            time.sleep(0.01)
        u.set_time_unknown_pps(uhd.time_spec(math.ceil(tt)+1.0))
        u.set_start_time(uhd.time_spec(next_time + self.args.clockoffset/1e6))
        u.set_samp_rate(self.args.sample_rate)
        u.set_center_freq(self.args.center_freq,0)

        if self.args.tune_args is not None:
            self.args.tune_args= list(self.args.tune_args.split(','))
            print ("HELLO",self.args.tune_args)
            try:
                tune_args_dict = dict([a.split('=') for a in self.args.tune_args])
            except ValueError:
                raise ValueError(
                    'Tune request arguments must be {KEY}={VALUE} pairs.'
                )
            self.args.tune_args = [
                '{0}={1}'.format(k, v) for k, v in tune_args_dict.items()
            ]
        #center freq
        tune_res= u.set_center_freq(uhd.tune_request(self.args.center_freq,
        self.args.lo_offsets,
         args=uhd.device_addr(','.join(self.args.tune_args)),
         ),
         0)
        # store actual values from tune result
        self.args.center_freq = (tune_res.actual_rf_freq + tune_res.actual_dsp_freq)
        self.args.lo_offsets = -tune_res.actual_dsp_freq

        print "Actual center freq %1.8f Hz"%(u.get_center_freq(0))
        print "===> self.args.gain: %s"%(self.args.gain)
        u.set_gain(self.args.gain, 0)
        u.set_antenna(self.args.txport, 0)
        #code_source = gr.file_source(gr.sizeof_gr_complex*1, self.args.codefile, True)
        code_vector = numpy.fromfile(self.args.codefile,dtype=numpy.complex64)
        code_source = blocks.vector_source_c(code_vector.tolist(), True)
        #multiply = gr.multiply_const_vcc((0.5, ))
        print "===> self.args.amplitude: %s"%(self.args.amplitude)
        multiply = blocks.multiply_const_vcc((self.args.amplitude, ))

        cr = u.get_clock_rate()
        print ("clockrate",cr)
        samplerate = u.get_samp_rate()
        srdec = int(round(cr / samplerate))
        samplerate_ld = numpy.longdouble(cr) / srdec
        sr_rat = Fraction(cr).limit_denominator() / srdec
        samplerate_num = sr_rat.numerator
        samplerate_den = sr_rat.denominator
        print ("samplerate_num",samplerate_num)
        print ("samplerate_den",samplerate_den)

        tb.connect(code_source, multiply, u)
        #        tb.connect((async_src, msg), (u_queue, 0))
        tb.start()
        self.print_info(u.get_usrp_info(0))
        print "Starting"
        print "Restart time: "+str(self.args.restart_time)
        while(True):
        	tnow = time.time()
        	if (tnow - tstart_tx) > self.args.restart_time:
        		tb.stop()
        		exit(0)
        	print (u.get_mboard_sensor("ref_locked"))
        	#if self.args.clocksource == "gpsdo":
        	#	txlog.write("%s %s\n"%(sampler_util.time_stamp(),u.get_mboard_sensor("gps_locked")))

        	# print('Sensors names:\n')
        	# print(u.get_mboard_sensor_names())
        	# print('\n')
        	#txlog.write("%s %s\n"%(sampler_util.time_stamp(),u.get_mboard_sensor("ref_locked")))
        	#txlog.write("%s %1.2f\n"%(sampler_util.time_stamp(),u.get_time_now().get_real_secs()))
        	txlog.write("%s\n"%(sampler_util.time_stamp()))
        	# if async_msgq.count(): The whole block was commented by Alejandro
        	# 	print("Have no sense \n")
        	# 	md = async_src.msg_to_async_metadata_t(async_msgq.delete_head())
        	# 	txlog.write("%s async Channel: %i Time: %f Event: %i" % (sampler_util.time_stamp(),md.channel, md.time_spec.get_real_secs(), md.event_code))
        	txlog.flush()
        	time.sleep(10.0)


if __name__ == '__main__':
    parser = ArgumentParser(prog="HF Transmitter", description="Configurable Transmitter\n")

    parser.add_argument("-a", "--address", dest="ip", type=str,action="store", default="172.16.5.189",
    help="Device address (ip number).")

    parser.add_argument("-r", "--samplerate", dest="sample_rate", type=float,action="store", default=1000000,help="Sample rate (Hz).")

    parser.add_argument("-t", "--rep", dest="rep", type=int,action="store",default=1, help="Repetition time (s)")

    parser.add_argument("-s", "--starttime", dest="start_time", type=int, action="store",
                      help="Start time (s)")

    parser.add_argument("-x", "--txport", dest="txport", type=str, action="store", default="TX/RX",
                      help="TX port")
    parser.add_argument("-g", "--gain", dest="gain", type=float, action="store", default=0.0,
                      help="Transmit gain (default 0.0 dB)")

    parser.add_argument("-c", "--centerfreq",dest="center_freq", action="store", type=float, default=2722167.96875,
                      help="Center frequency (default 1.9e6)")

    parser.add_argument("-f", "--codefile",dest="codefile", action="store", type=str,
                      help="Transmit code file.")
    parser.add_argument("-b", "--clocksource",dest="clocksource", action="store", type=str, default="gpsdo",
                      help="Clock source (default gpsdo).")
    parser.add_argument("-o", "--clockoffset",dest="clockoffset", action="store", type=float, default=0.0,
                      help="Clock offset in microseconds (default 0.0 us).")
    parser.add_argument("-z", "--restart",dest="restart_time", action="store", type=float, default=3600.0,
                      help="Restart every n seconds, to realign clock (default 3600 s).")
    parser.add_argument("-p", "--amplitude", dest="amplitude", type=float, action="store", default=1,
                      help="Amplitude factor [0,1] (default 0.25)")

    parser.add_argument('-T', '--tuneargs', dest='tune_args', action="store",default="",
        help='''Tune request arguments, e.g. "mode_n=integer,int_n_step=100e3".
                (default: '')''',)

    parser.add_argument('-F', '--lo_offset', dest='lo_offsets', action="store", type=float,default=0.0,
        help='''Frontend tuner offset from center frequency, in Hz.
                (default: 0)''',
                )

    args = parser.parse_args()
    #self.args.ip = "192.168.10.2"
    #self.args.recv_buff_size = 100000
    #self.args.send_buff_size = 100000

    if args.start_time == None:
        args.start_time = math.ceil(time.time())

    if args.codefile == None:
    	args.codefile = "/home/alex/HaystackOP/waveforms/code-l10000-b10-000000.bin"


    tx = meteor_transmit(args)
    tx.start()
