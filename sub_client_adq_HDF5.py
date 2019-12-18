import numpy
import sys
import zmq
import time

port ="5556"
if len(sys.argv)>1:
    port = sys.argv[1]
    int(port)

if len(sys.argv)>2:
    port1 = sys.argv[2]
    int(port1)


#Socket to talk to server
context = zmq.Context()
socket  = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:%s"%port)

if len(sys.argv)>2:
    socket.connect("tcp://localhost:%s"%port1)

#Subscribe to zipcode, default is NYC,10001
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE,topicfilter)
#Process 5 updates
total_value=0
count= -1
azi= []
elev=[]
time0=[]
#for update_nbr in range(250):
while(True):
    string= socket.recv()
    #topic,ang_elev,ang_azi,seconds= string.split()
    topic,ang_elev,ang_elev_dec,ang_azi,ang_azi_dec,seconds,seconds_dec= string.split()
    #seconds = struct.unpack('!d', data)
    ang_azi =float(ang_azi)+1e-3*float(ang_azi_dec)
    ang_elev =float(ang_elev)+1e-3*float(ang_elev_dec)
    seconds =float(seconds) +1e-6*float(seconds_dec)
    azi.append(ang_azi)
    elev.append(ang_elev)
    time0.append(seconds)
    count +=1
    print (count,topic,"AE°:",ang_elev,"AA°",ang_azi,"T",seconds)
    if count == 36000:
        pedestal_array=numpy.array([azi,elev,time0])
        count=0
        azi= []
        elev=[]
        time0=[]
        print(pedestal_array[0][0][0])
        time.sleep(4)
    #print (topic,"AE°:",ang_elev,"AA°",ang_azi,"T",seconds)

print ("Average messagedata value for topic '%s' was %dF" % ( topicfilter,total_value / update_nbr))
