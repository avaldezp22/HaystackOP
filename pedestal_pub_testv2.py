###########################################################################
############################### SERVIDOR###################################
######################### SIMULADOR DE PEDESTAL############################
###########################################################################

import time
import math
import numpy
import struct
from time import sleep
import zmq
import pickle


port="5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s"%port)

###### PARAMETROS DE ENTRADA################################
print("PEDESTAL RESOLUCION 0.01")
print("MAXIMA VELOCIDAD DEL PEDESTAL")
ang_elev = 4.12
ang_azi  = 30

velocidad= input ("Ingresa velocidad:")
velocidad= float(velocidad)
print (velocidad)
############################################################

##############################################################
# ECUACION POLINOMIAL DE 7mo Grado
##############################################################
a=  -2.60395*1e-8
b=  2.29869*1e-6
c=  -8.47469*1e-5
d=  16.9267*1e-4
e=  -19.8717*1e-3
f=  0.139122
g=  -0.561741
h=  1.18433
v= velocidad
delay= a*v**7 +b*v**6 +c*v**5 +d*v**4+e*v**3+f*v**2+g*v+h
##############################################################

print("delay in program",delay)
sleep(3)
print("start program")

while(True):
    t1 = time.time()
    for i in range(359):
        for j in range(100):
            ang_azi  = i+j/100.0
            seconds  = time.time()
            topic=10001
            print ("Topic: ",topic,"Elev°: ",ang_elev,"Azim°: ",ang_azi,"Time:" ,seconds)
            seconds_dec=(seconds-int(seconds))*1e6
            ang_azi_dec= (ang_azi-int(ang_azi))*1e3
            ang_elev_dec=(ang_elev-int(ang_elev))*1e3
            #print(seconds_dec)
            #data= struct.pack('!d',seconds)
            #socket.send_string(topic,data)
            #socket.send_string(topic,seconds)

            socket.send_string("%d %d %d %d %d %d %d"%(topic,ang_elev,ang_elev_dec,ang_azi,ang_azi_dec,seconds,seconds_dec))
        sleep(delay)# delay ---->   0.0477,Velocity--- 19.99 °/seg Para disminuir velocidad aumentar delay
    t2 = time.time()
    print ("Total time for 360° in Seconds",t2-t1,"V °/seg",360/(t2-t1),"V rad/seg", 2*math.pi/(t2-t1),"delay",delay)
    time.sleep(10)
