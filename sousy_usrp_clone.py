#!/usr/bin/env python
#
# Simple usrp sampler to be used with the following setup:
# - four usrp2-series devices. 
# - external 1 PPS and 10 MHz
# - <0.1 s computer clock error (e.g., use network time protocol)
#
# (c) 2014 Juha Vierinen 
#
import time
import numpy
import ast
from optparse import OptionParser
import sys, time, os, math, re
import juha
import sampler_util

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio import filter 
from gnuradio.filter import firdes 

debug = True
__C = 299792458     #Speed of light m/s

parser = OptionParser(option_class=eng_option)

parser.add_option("-a", "--args", type="string", default="",
                  help="UHD device address args [default=%default]")

parser.add_option("", "--spec", type="string", default="A:A A:B",
              help="Subdevice of UHD device where appropriate")

parser.add_option("-c", "--centerfreq",dest="centerfreq", action="store",
                  type="float",
                  #default=100.0e6-46502493.880689144,
                  default=21484375,
                  help="Center frequency (default %default)")

parser.add_option("-r", "--samplerate",dest="samplerate", action="store",
                  type="eng_float", 
                  #default=4e6,
                  default=200000, #(5us baud)
                  #default=100000, #(10us baud) NO SE PUEDE CON 100k
                  help="Sample rate (default %default Hz)")

parser.add_option("-n", "--name",dest="name", action="store",
                  #default="/media/usrp/data_sousy/USRP_60KM/",
                  default='/media/usrp/data_sousy/RAWDATACIRI2CH',
                  type="string",
                  help="Prefix of data directory.")

parser.add_option("-s", "--sync",dest="sync", action="store_true",
                  default=True,
                  help="Sync to external clock.")

parser.add_option("", "--nchannels",dest="nchannels", action="store",
		  type="int",#new
                  #default=1,
                  default=2,
                  help="number of channels")

parser.add_option("", "--timezone",dest="timezone", action="store",
                  default=time.timezone,
                  help="local timezone")

parser.add_option("", "--code",dest="code", action="store",
                  #default=None,
                  #default='[1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1]',
                  default='[1,1,-1,1, 1, -1, 1, -1,-1, 1,-1, -1, -1, 1, -1, -1, -1, 1, -1, -1,-1, 1, 1, 1, 1,-1, -1, -1]',
                  type="string",
                  help="pulse code, it can has nCode > 1 and nBaud > 1. Example: [1,1,-1], [-1,-1,1] (nCode=3 and nBaud=2)")
#default ="[1],[-1]"

parser.add_option("", "--ipp",dest="ipp", action="store",
                  #default=400e-6, 
                  default=8000e-6,
                  type="float",
                  help="ipp in seconds")


(op, args) = parser.parse_args()

#op.mboards = op.mboards.split(",")

op.starttime = None
op.period = 1
print "op.code",op.code

if op.code == None:
    print "Alex 5 CODE NONE"
    codeType = 0
    nCode = 0
    nBaud = 0
    code = 0
else:
    codeType = 1
    code_list = ast.literal_eval(op.code)
    code = numpy.asarray(code_list)
    
    if code.ndim == 1:
        nCode = 1
        nBaud = len(code)
    else:
        nCode = code.ndim
        nBaud = len(code[0])
 
# create usrp source block

u = uhd.usrp_source(
                    device_addr=op.args,
                    stream_args=uhd.stream_args(cpu_format="fc32",
                                                channels=range(op.nchannels)
                                                )
                     )

# Set the subdevice spec
if(op.spec):
    #u.set_subdev_spec(op.spec, 0)
    u.set_subdev_spec(op.spec) 
    print "ALEX1"
else:
    op.spec = u.get_subdev_spec()
            
# for each usrp
#u.set_subdev_spec("A:A A:B")
for i in range(1):
    # set clock source
    if op.sync:
        u.set_clock_source("external",i)
        u.set_time_source("external",i)
	print "ALEX2"
    else:
        u.set_clock_source("internal",i)
        u.set_time_source("none",i)
    # setup RX-A and RX-B as analog inputs for the two channels
    # u.set_subdev_spec("A:B",i)
    #u.set_subdev_spec("A:A A:B")
    

##NEW###

#####

# set sample rate
u.set_samp_rate(op.samplerate)
print
print "Samp rate: %f Msps" % (u.get_samp_rate()/1e6)
print

# while True:
#     x  = u.get_time_last_pps()
#     print "last pps time: ", x.get_real_secs()
#     time.sleep(0.3)

# synchronize to network clock (needs to be < 0.3 from absolute time
if op.sync:
    print "Alex3"
    tt = time.time()
    while tt-math.floor(tt) < 0.2 or tt-math.floor(tt) > 0.3:
        tt = time.time()
        time.sleep(0.01)
    print("Latching at "+str(tt))
    # when pps seen, set device clock to correct absolute full seconds
    u.set_time_unknown_pps(uhd.time_spec(math.ceil(tt)+1.0))
    time.sleep(1)

pps_time = u.get_time_last_pps()

print "PPS detected at %s" %str(pps_time.get_real_secs())

if op.starttime is None:
    op.starttime = math.ceil(time.time())+5

# we assume that our experiment has a repeat cycle, and we wait until the start of the next repeat cycle 
#op.starttime = sampler_util.find_next(op.starttime,op.period)
# start sampling at this unix second
if op.sync:
    print("Starting acquisition at "+str(op.starttime))
    u.set_start_time(uhd.time_spec(op.starttime))

# set center frequencies
for i in range(op.nchannels):
    
    u.set_gain(10, i)
    u.set_bandwidth(10e3, i)
    
    #print "Gain: ", u.get_gain(), u.get_gain_names(i), u.get_gain_range()
    print "Gain: ", u.get_gain()
    print "BW: ", u.get_bandwidth(i), u.get_bandwidth_range(i)
    
#     print u.set_center_freq(46502477.303147316,i)
    print u.set_center_freq(op.centerfreq,i)
    
    print "Center frequency %d = %f MHz" %(i, u.get_center_freq(i)/1e6)
    
print

# create flowgraph
fg = gr.top_block()

for i in range(op.nchannels):
    dname = "%s/ch%03d"%(op.name,i)
    os.system("mkdir -p %s"%(dname))
    # write global metadata for channel
    sampler_util.write_metadata_drf(dname,
                                    1,
                                    op.centerfreq,
                                    op.starttime,
                                    dtype="<f4",
                                    itemsize=8,
                                    sr=op.samplerate,
                                    extra_keys=["usrp_ip", "timezone", "codeType", "nCode", "nBaud", "code", "ipp"],
                                    extra_values=[op.spec, op.timezone, codeType, nCode, nBaud, code, op.ipp])

    dst = juha.digital_rf(dname,
                          int(op.samplerate),
                          int(3600),
                          gr.sizeof_gr_complex,
                          op.samplerate)

    # connect flowgraph
    fg.connect((u, i), (dst,0))

if debug:
    print "Starting at %d"%(op.starttime)
    
fg.start()

while(True):
    time.sleep(1)
