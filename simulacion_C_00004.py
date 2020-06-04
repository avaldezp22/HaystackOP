################### RESUMEN DEL PROGRAMA DE ADQUISICION ###############################
import numpy
import math
import random
import time
import matplotlib
import matplotlib.pyplot as plt

# input:
#   m_nBauds
#   m_nNum_Codes
#   Dyn_snCode
#   FixRCP_m_fTXB
#   m_nSamples
#   Rebuff
#   Imbuff
#   InBuffer

#################################################################
##################### plot_cts
################################################################

def plot_cts(x,H0,DH0,plot_abs=False,plot_draw=True,plot_show=False):
    time_vec = DH0*numpy.linspace(0, len(x)-1,num=len(x)) +H0
    print(time_vec)
    fig = plt.figure()
    plt.plot(time_vec, numpy.real(x),"blue")
    plt.plot(time_vec, numpy.imag(x),"red")
    if plot_abs:
        plt.plot(time_vec,numpy.abs(x),"cyan")
    if plot_draw:
        plt.draw()
        plt.waitforbuttonpress(0)
        plt.close(fig)
    if plot_show:
        plt.show()

def wave_fft(x,plot_show=False):
    fft = numpy.fft.fft(x)
    fft = numpy.fft.fftshift(fft)
    fft = fft / numpy.max(numpy.abs(fft))
    #fft = np.abs(fft)**2.0
    plot_draw= not (plot_show)
    plot_cts(fft,0,1,plot_draw=plot_draw,plot_show=plot_show)


#################################################################
##################### init_pulse
################################################################
        
def init_pulse(m_nNum_Codes,m_nBauds,BaudWidth,Dyn_snCode):
    fAngle                            = 2.0*math.pi*(1/16)
    DC_level                          = 500
    stdev                             = 8
    m_nNum_Codes= m_nNum_Codes
    m_nBauds    = m_nBauds
    BaudWidth   = BaudWidth
    Dyn_snCode  = Dyn_snCode

    if m_nBauds:
        pulses    = list(range(0,m_nNum_Codes))
        num_codes = m_nNum_Codes
        for i in range(num_codes):
            pulse_size = m_nBauds*BaudWidth
            pulses[i]  = numpy.zeros(pulse_size)
            for j in range(m_nBauds):
                for k in range(BaudWidth):
                    pulses[i][j*BaudWidth+k] = int(Dyn_snCode[i][j]*600)
    else:
        pulses     = list(range(1))
        pulse_size = int(FixRCP_m_fTXB/0.15+0.5)
        pulses[0]  = numpy.ones(pulse_size)
        pulses     = 600*pulses[0]
    return pulses,num_codes,pulse_size


#################################################################
##################### Generate block data
################################################################
# m_nChannels
# prof_gen
#    fAngle                            = 2.0*math.pi*(1/16)
#    DC_level                          = 500
#    stdev
#    num_codes
fAngle                            = 2.0*math.pi*(1/16)
num_codes                      = 8

def jro_GenerateBlockOfData(m_nSamples,DC_level,stdev,m_nReference,pulses,num_codes,pulse_size,prof_gen,H0,DH0):
    m_nSamples = m_nSamples
    DC_level   = DC_level
    stdev      = stdev
    m_nR       = m_nReference
    pulses     = pulses
    num_codes  = num_codes
    ps         = pulse_size
    prof_gen   = prof_gen
    H0         = H0
    DH0        = DH0
    fAngle                            = 2.0*math.pi*(1/16)

    # NOISE
    Seed_r=random.seed(2)
    Noise_r = numpy.random.normal(DC_level,stdev,m_nSamples)
    Seed_i=random.seed(3)
    Noise_i = numpy.random.normal(DC_level,stdev,m_nSamples)
    Noise   = numpy.zeros(m_nSamples,dtype=complex)
    Noise.real = Noise_r
    Noise.imag = Noise_i
    Pulso     = numpy.zeros(pulse_size,dtype=complex)

    #DOPPLER
    x          = m_nSamples
    time_space = (DH0*numpy.linspace(0, x-1,num=x) +H0)
    time_vec   = time_space*(1.0e-3/150.0)
    fd         = 10
    d_signal   = numpy.array(numpy.exp(1.0j*2.0*math.pi*fd*time_vec),dtype=numpy.complex64)


    
    for i in range(m_nChannels):
        for k in range(prof_gen):
            Pulso.real =  pulses[k%num_codes]
            Pulso.imag =  pulses[k%num_codes]
            
            InBuffer   = numpy.zeros(m_nSamples,dtype=complex)
            
            InBuffer[m_nR:m_nR+ps] = Pulso

            InBuffer = Noise+ InBuffer

            InBuffer.real[m_nR:m_nR+ps] = InBuffer.real[m_nR:m_nR+ps]*(math.cos( fAngle)*5) 
            InBuffer.imag[m_nR:m_nR+ps] = InBuffer.imag[m_nR:m_nR+ps]*(math.sin( fAngle)*5)

            InBuffer=InBuffer
            #print(InBuffer[:10])
            #print(InBuffer.shape)
            plot_cts(InBuffer,H0=H0,DH0=DH0)
            #wave_fft(x=InBuffer,plot_show=True)
            #time.sleep(1)

            
#############################################
############## INIT_ACQUISITION##############
#############################################
incIntfactor                      = 1    # G
m_nFFTPoints                      = 0    # G
m_nProfilesperBlock               = 300  # G
FixPP_m_nIncoherentIntegrations   = 1    # G
FixRCP_m_fIPP                     = 1000 # G
FixPP_m_n_CoherentIntegrations    = 1
Dyn_sfTau_0                       = 250
Dyn_sfAcqH0_0                     = 70
H0                                = Dyn_sfAcqH0_0
Dyn_sfAcqDH_0                     = 1.25
DH0                               = Dyn_sfAcqDH_0
m_nBauds                          = 32
FixRCP_m_fTXA                     = 40

fAngle                            = 2.0*math.pi*(1/16)
DC_level                          = 500
stdev                             = 8
m_nNum_Codes                      = 2
code0                             =numpy.array([1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1])
code1                             =numpy.array([1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0])
Dyn_snCode                        = numpy.array([code0,code1])
m_nSamples                        = 200
m_nChannels                       = 1

if m_nFFTPoints != 0:
    incIntfactor = m_nProfilesperBlock/m_nFFTPoints
    if (FixPP_m_nIncoherentIntegrations> incIntfactor):
        incIntfactor = FixPP_m_nIncoherentIntegrations/ incIntfactor
    elif(FixPP_m_nIncoherentIntegratios< incIntfactor):
        print("False alert...")

timeperblock =int(((FixRCP_m_fIPP
                    *m_nProfilesperBlock
                    *FixPP_m_n_CoherentIntegrations
                    *incIntfactor)
                    /150.0)
                    *0.9
                    +0.5)
# para cada canal
prof_gen     =   m_nProfilesperBlock*FixPP_m_n_CoherentIntegrations
prof_gen     =   m_nProfilesperBlock

m_nReference = int((Dyn_sfTau_0-Dyn_sfAcqH0_0)/(Dyn_sfAcqDH_0)+0.5)
print(m_nReference)
BaudWidth    =  int((FixRCP_m_fTXA/Dyn_sfAcqDH_0)/m_nBauds + 0.5 )
print(BaudWidth)
if (BaudWidth==0):
    BaudWidth=1
pulses, num_codes,pulse_size= init_pulse(m_nNum_Codes=m_nNum_Codes,m_nBauds=m_nBauds,BaudWidth=BaudWidth,Dyn_snCode=Dyn_snCode)

jro_GenerateBlockOfData(m_nSamples=m_nSamples,DC_level=DC_level, stdev=stdev
                                ,m_nReference=m_nReference,pulses=pulses,num_codes= num_codes,pulse_size=pulse_size,prof_gen=prof_gen,H0=H0,DH0=DH0 )
