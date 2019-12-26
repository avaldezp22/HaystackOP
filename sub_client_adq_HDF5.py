import numpy
import sys
import zmq
import time
import h5py
import os

path="/home/soporte/Downloads/pedestal"
ext=".hdf5"

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
    #print (count,topic,"AE°:",ang_elev,"AA°",ang_azi,"T",seconds)
    if count == 6000:
        timetuple=time.localtime()
        epoc = time.mktime(timetuple)
        fullpath = path + ("/" if path[-1]!="/" else "")


        if not os.path.exists(fullpath):
            os.mkdir(fullpath)

        azi_array  = numpy.array(azi)
        elev_array = numpy.array(elev)
        time0_array= numpy.array(time0)
        pedestal_array=numpy.array([azi,elev,time0])
        count=0
        azi= []
        elev=[]
        time0=[]
        print(pedestal_array[0])
        print(pedestal_array[1])

        meta='PE'
        filex="%s%4.4d%3.3d%10.4d%s"%(meta,timetuple.tm_year,timetuple.tm_yday,epoc,ext)
        filename = os.path.join(fullpath,filex)
        fp = h5py.File(filename,'w')
        print("Escribiendo HDF5...")
        dset = fp.create_dataset("pedestal", data=pedestal_array)
        fp.close()

        time.sleep(4)
    #print (topic,"AE°:",ang_elev,"AA°",ang_azi,"T",seconds)

print ("Average messagedata value for topic '%s' was %dF" % ( topicfilter,total_value / update_nbr))
