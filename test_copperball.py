import numpy
import math

nsamples   = 60
code       = 1 
pulse_size = numpy.ones(nsamples)



phases= numpy.array(numpy.exp(1.0j * 2.0 * math.pi * pulse_size),dtype=numpy.complex64)
print("show",pulse_size)
print("showf", phases)
 
