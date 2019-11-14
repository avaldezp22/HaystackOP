import time
import math

from time import sleep

print("PEDESTAL RESOLUCION 0.01")
print("MAXIMA VELODAD DEL PEDESTAL")

ang_elev = 4 
ang_azi  = 30


while(True):
    t1 = time.time()
    for i in range(359):
        for j in range(100):
            ang_azi  = i+j/100.0
            seconds  = time.time()
            print ("Elev: ",ang_elev,"Azim: ",ang_azi,"Time:" ,seconds)
        sleep(0.06)# delay ---->   0.0477,Velocity--- 19.99 °/seg Para disminuir velocidad aumentar delay
    t2 = time.time()
    print ("Total time for 360° in Seconds",t2-t1,"V °/seg",360/(t2-t1),"V rad/seg", 2*math.pi/(t2-t1))
    time.sleep(10)

