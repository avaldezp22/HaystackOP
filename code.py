#!/usr/bin/env python
import numpy
code_vector = numpy.fromfile('/home/alex/digital_rf/python/examples/sounder/waveforms/code-l10000-b10-000000.bin',dtype=numpy.complex64)
code_0 = code_vector.tolist()
