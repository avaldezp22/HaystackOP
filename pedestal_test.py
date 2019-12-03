import time
import math

from time import sleep

print("PEDESTAL RESOLUCION 0.01")
print("MAXIMA VELOCIDAD DEL PEDESTAL")

ang_elev = 4
ang_azi  = 30

velocidad= input ("Ingresa velocidad:")
velocidad= float(velocidad)
print (velocidad)

# ECUACION POLINOMIAL DE 4TO Grado
a= -2.85622*1e-8
b= 2.5068*1e-6
c= -9.16486*1e-5
d= 18.1067*1e-4
e= -20.9816*1e-3
f= 0.144797
g= -0.57621
h= 1.19849
v= velocidad
delay= a*v**7 +b*v**6 +c*v**5 +d*v**4+e*v**3+f*v**2+g*v+h

print("delay in program",delay)
sleep(1)
print("start program")

while(True):
    t1 = time.time()
    for i in range(359):
        for j in range(100):
            ang_azi  = i+j/100.0
            seconds  = time.time()
            print ("Elev: ",ang_elev,"Azim: ",ang_azi,"Time:" ,seconds)
        sleep(delay)# delay ---->   0.0477,Velocity--- 19.99 °/seg Para disminuir velocidad aumentar delay
    t2 = time.time()
    print ("Total time for 360° in Seconds",t2-t1,"V °/seg",360/(t2-t1),"V rad/seg", 2*math.pi/(t2-t1),"delay",delay)
    time.sleep(10)
