################################################
### ESTA ES  LA CLASE INIT PULSE################
################################################
####EN EL REAL QUE VAMOS A CREAR EXISTE UN ANGULO
import numpy
import math

#typedef signed short   Ipp16s;
#    Ipp16s  re;
#    Ipp16s  im;

# x=range(0,2) ####0, n-1
# list(x)
# 0,1

# m_nBauds      # numero de baudios
# n_nNum_Codes  # numero de codigos
##############################################################
# Pendiente de declarar
##############################################################
#m_nBauds
#m_nNum_Codes
#BaudWidth
#m_nSamples
#Dyn_snCode
#FixRCP_m_fTXB

# IPPAPI( Ipp16s*,  ippsMalloc_16s, (int len) )

###########################################################
################## INIT_ACQUISITION#############################
###########################################################
# m_nProfilesperBlock=
# m_nFFTPoints
# FixRCP_m_fIPP
# FixPP_m_n_CoherentIngrations
# Dyn_sfTau
# Dyn_sfAcqH0
# Dyn_sfAcqDH
# FixRCP_m_fTXA
# Dyn_sfAcqDH
# m_nBauds

print("START ACQUISITION")
incIntfactor=1
if m_nFFTPoints!=0:
    incIntfactor = m_nProfilesperBlock/m_nFFTPoints

    if (FixPP_m_nIncoherentIntegratios > incIntfactor):
        incIntfactor = FixPP_m_nIncoherentIntegratios> incIntfactor
    elif(FixPP_m_nIncoherentIntegratios< incIntfactor):
        print("menor")

timeperblock =int((FixRCP_m_fIPP*m_nProfilesperBlock*FixPP_m_n_CoherentIngrations*incIntfactor*0.9/150.0)+0.5)
## para cada canal
prof_gen     = m_nProfilesperBlock* FixPP_m_n_CoherentIngrations

proge_gen    = m_nProfilesperBlock

m_nReference = ((Dyn_sfTau[0] - Dyn_sfAcqH0[0])/(Dyn_sfAcqDH[0])+0.5)

BaudWidth    = int((FixRCP_m_fTXA/Dyn_sfAcqDH[0])/m_nBauds+0.5)

if(BaudWidth==0):
    BaudWidth =1
#### AQUI SE LLAMA A INIT_PULSES

###########################################################
################## INIT_PULSES#############################
###########################################################

FANGLE  = 2.0*math.pi*(1/16.0)  #####el angulo entre la parte real e imaginaria
DC_LEVEL= 500.0                   ##### 2000, promedio del ruido gaussiano
STDV    = 8.0                     #####2048, desviacion estandar del ruido gaussiano

if m_nBauds>0: # si es mayor que 0
    pulses    = list(range(0,m_nNum_Codes))
    num_codes = m_nNum_Codes
    for i in range(m_nNum_Codes):         # Dependiendo del numero de codigos
        pulse_size = m_nBauds*BaudWidth
        pulses[i] = numpy.zeros(pulse_size)
        for j in range(m_nBauds):
            for k in range(BaudWidth);
                pulses[i][j*BaudWidth+k] = int(Dyn_snCode[i][j]*600)
else:
    pulses     = list(range(1))
    pulse_size = int(FixRCP_m_fTXB/0.15 + 0.5)
    ones=600
    pulses[0]  =numpy.zeros(pulse_size)
    ippset= 600*pulses[0]

Rebuff = numpy.zeros(m_nSamples)
Imbuff = numpy.zeros(m_nSamples)
Noise  = numpy.zeros(m_nSamples)
#ippsZero_Rebuff =
#ippsZero_Imbuff =

#################################################################
##################### Generate block data
################################################################

# Acqbuffer
# seed
# Seed_time
InBuffer = numpy.array(,dtype=complex)
for i in range(m_nChannels):
    for k in range(prof_gen):
        # DENTRO DE CADA PERFIL
        #srand(Seed_Time.LowPart)
        #Seed = (unsigned int)rand()
        #AQUI TENGO QUE DECLARAR samples, mean,stdev
        Seed=random.seed(2)
        # numpy.random.normal(m,s,size=N)
        IppsRandGauss_Direct_16s = numpy.random.normal(DC_LEVEL,stdev,m_nSamples)
        #ippsCopy_16s(pulses[profile%num_codes],&Rebuff[m_nReference],pulse_size);
        Rebuff[m_nReference] = pulses[k%num_codes]*(cos(fAngle)*5)
        Imbuff[m_nReference] = pulses[k%num_codes]*(sin(fAngle)*5)
        #ippsAdd_16s_I(Noise,Rebuff,MyExpParam->MySystemParam.m_nSamples);
        InBuffer = numpy.ones(m_nSamples,dtype=complex)
        Re[InBuffer] = Rebuff
        Im[InBuffer] = ippsZero_Imbuff

        InBuffer += m_nSamples
