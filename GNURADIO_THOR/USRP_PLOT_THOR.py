#!python
'''
'''
import os, sys
import datetime
import time

path = os.path.dirname(os.getcwd())
path = os.path.dirname(path)
sys.path.insert(0, path)

from schainpy.controller import Project

desc = "USRP_test"
filename = "USRP_processing.xml"
controllerObj = Project()
controllerObj.setup(id = '191', name='Test_USRP', description=desc)

############## USED TO PLOT IQ VOLTAGE, POWER AND SPECTRA #############

#######################################################################
######PATH DE LECTURA, ESCRITURA, GRAFICOS Y ENVIO WEB#################
#######################################################################
#path = '/media/data/data/vientos/57.2063km/echoes/NCO_Woodman'


#path = '/home/alex/data3/'
#path = '/home/alex/data_w/'   #### with clock 28.6 dB noise  
#path = '/home/alex/data_w12/' #### with clock 35.27 dB noise 
path = '/home/alex/data_wgcc/' #### with clock   35.16 db noise
#path = '/home/alex/data_wgwc/' #### without  clock
#path = '/home/alex/data_wto/'  #### turn off generator -2.86 dB noise
#wr_path = '/media/usrp/data_sousy/RAWDATACIRI2CH/pdata'
figures_path = '/home/alex/data_plot'
#remotefolder = "/home/wmaster/graficos"
#######################################################################
################# RANGO DE PLOTEO######################################
#######################################################################
dBmin = '30'
dBmax = '60'
xmin = '0'
xmax ='24'
ymin = '0'
ymax = '600'
#######################################################################
########################FECHA##########################################
#######################################################################
str = datetime.date.today()
today = str.strftime("%Y/%m/%d")
str2 = str - datetime.timedelta(days=1)
yesterday = str2.strftime("%Y/%m/%d")
#######################################################################
######################## UNIDAD DE LECTURA#############################
#######################################################################
readUnitConfObj = controllerObj.addReadUnit(datatype='DigitalRFReader',
                                            path=path,
                                            startDate="2019/07/02",#today,
                                            endDate="2109/07/03",#today,
                                            startTime='00:00:00',
                                            endTime='23:59:59',
                                            delay=0,
                                            #set=0,
                                            online=0,
                                            walk=1,
                                            ippKm = 1500)

opObj11 = readUnitConfObj.addOperation(name='printInfo')
opObj11 = readUnitConfObj.addOperation(name='printNumberOfBlock')
#######################################################################
################ OPERACIONES DOMINIO DEL TIEMPO########################
#######################################################################

procUnitConfObjA = controllerObj.addProcUnit(datatype='Voltage', inputId=readUnitConfObj.getId())
#
# codigo64='1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,'+\
#              '1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1'

opObj11 = procUnitConfObjA.addOperation(name='setRadarFrequency')
opObj11.addParameter(name='frequency', value='30e6', format='float')

opObj10 = procUnitConfObjA.addOperation(name='Scope', optype='external')
opObj10.addParameter(name='id', value='10', format='int')
#opObj10.addParameter(name='xmin', value='0', format='int')
#opObj10.addParameter(name='xmax', value='50', format='int')
opObj10.addParameter(name='type', value='iq')
opObj10.addParameter(name='ymin', value='-5000', format='int')
#opObj10.addParameter(name='ymax', value='8500', format='int')

#opObj10 = procUnitConfObjA.addOperation(name='setH0')
#opObj10.addParameter(name='h0', value='-5000', format='float')

#opObj11 =  procUnitConfObjA.addOperation(name='filterByHeights')
#opObj11.addParameter(name='window', value='1', format='int')

#codigo='1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,-1'
#opObj11 = procUnitConfObjSousy.addOperation(name='Decoder', optype='other')
#opObj11.addParameter(name='code', value=codigo, format='floatlist')
#opObj11.addParameter(name='nCode', value='1', format='int')
#opObj11.addParameter(name='nBaud', value='28', format='int')

#opObj11 = procUnitConfObjA.addOperation(name='CohInt', optype='other')
#opObj11.addParameter(name='n', value='100', format='int')

#######################################################################
########## OPERACIONES DOMINIO DE LA FRECUENCIA########################
#######################################################################
procUnitConfObjSousySpectra = controllerObj.addProcUnit(datatype='Spectra', inputId=procUnitConfObjA.getId())
procUnitConfObjSousySpectra.addParameter(name='nFFTPoints', value='100', format='int')
procUnitConfObjSousySpectra.addParameter(name='nProfiles', value='100', format='int')
#procUnitConfObjSousySpectra.addParameter(name='pairsList', value='(0,0),(1,1),(0,1)', format='pairsList')

#opObj13 = procUnitConfObjSousySpectra.addOperation(name='removeDC')
#opObj13.addParameter(name='mode', value='2', format='int')

#opObj11 = procUnitConfObjSousySpectra.addOperation(name='IncohInt', optype='other')
#opObj11.addParameter(name='n', value='60', format='float')
#######################################################################
########## PLOTEO DOMINIO DE LA FRECUENCIA#############################
#######################################################################

#opObj11 = procUnitConfObjSousySpectra.addOperation(name='RTIPlot', optype='other')
#opObj11.addParameter(name='id', value='101', format='int')
#opObj11.addParameter(name='wintitle', value='RTIPlot', format='str')
#opObj11.addParameter(name='zmin', value=dBmin, format='int')
#opObj11.addParameter(name='zmax', value=dBmax, format='int')
#opObj11.addParameter(name='ymin', value=ymin, format='int')
#opObj11.addParameter(name='ymax', value=ymax, format='int')
#opObj11.addParameter(name='xmin', value=xmin, format='float')

#opObj11.addParameter(name='xmax', value=xmax, format='float')
#opObj11.addParameter(name='showprofile', value='0', format='int')
#opObj11.addParameter(name='save', value='1', format='int')
##opObj11.addParameter(name='figfile', value='rti0_sousy.png', format='str')
#opObj11.addParameter(name='figpath', value=figures_path, format='str')
#opObj11.addParameter(name='ftp', value='1', format='int')
#opObj11.addParameter(name='wr_period', value='2', format='int')
#opObj11.addParameter(name='exp_code', value='17', format='int')
#opObj11.addParameter(name='sub_exp_code', value='1', format='int')
#opObj11.addParameter(name='ftp_wei', value='0', format='int')
#opObj11.addParameter(name='plot_pos', value='0', format='int')

#SpectraPlot

opObj11 = procUnitConfObjSousySpectra.addOperation(name='SpectraPlot', optype='other')
opObj11.addParameter(name='id', value='1', format='int')
opObj11.addParameter(name='wintitle', value='Spectra', format='str')
#opObj11.addParameter(name='xmin', value=-0.01, format='float')
#opObj11.addParameter(name='xmax', value=0.01, format='float')
#opObj11.addParameter(name='zmin', value=dBmin, format='int')
#opObj11.addParameter(name='zmax', value=dBmax, format='int')
#opObj11.addParameter(name='ymin', value=ymin, format='int')
#opObj11.addParameter(name='ymax', value=ymax, format='int')
opObj11.addParameter(name='save', value='0', format='bool')
opObj11.addParameter(name='figpath', value = figures_path, format='str')
opObj11.addParameter(name='ftp', value='1', format='int')
# opObj11.addParameter(name='wr_period', value='2', format='int')
opObj11.addParameter(name='exp_code', value='17', format='int')
opObj11.addParameter(name='sub_exp_code', value='1', format='int')
# opObj11.addParameter(name='plot_pos', value='0', format='int')


# opObj11 = procUnitConfObjSousySpectra.addOperation(name='CrossSpectraPlot', optype='other')
# opObj11.addParameter(name='id', value='3', format='int')
# opObj11.addParameter(name='wintitle', value='CrossSpectraPlot', format='str')
# opObj11.addParameter(name='ymin', value=ymin, format='int')
# opObj11.addParameter(name='ymax', value=ymax, format='int')
# opObj11.addParameter(name='phase_cmap', value='jet', format='str')
# opObj11.addParameter(name='zmin', value=dBmin, format='int')
# opObj11.addParameter(name='zmax', value=dBmax, format='int')
# opObj11.addParameter(name='figpath', value=figures_path, format='str')
# opObj11.addParameter(name='save', value=0, format='bool')
# opObj11.addParameter(name='pairsList', value='(0,1)', format='pairsList')
# #
# opObj11 = procUnitConfObjSousySpectra.addOperation(name='CoherenceMap', optype='other')
# opObj11.addParameter(name='id', value='4', format='int')
# opObj11.addParameter(name='wintitle', value='Coherence', format='str')
# opObj11.addParameter(name='phase_cmap', value='jet', format='str')
# opObj11.addParameter(name='xmin', value=xmin, format='float')
# opObj11.addParameter(name='xmax', value=xmax, format='float')
# opObj11.addParameter(name='figpath', value=figures_path, format='str')
# opObj11.addParameter(name='save', value=0, format='bool')
# opObj11.addParameter(name='pairsList', value='(0,1)', format='pairsList')
#
# #send to server
# procUnitConfObj2 = controllerObj.addProcUnit(name='SendToServer')
# procUnitConfObj2.addParameter(name='server', value='jro-app.igp.gob.pe', format='str')
# #procUnitConfObj2.addParameter(name='server', value='10.10.120.125', format='str')
# procUnitConfObj2.addParameter(name='username', value='wmaster', format='str')
# procUnitConfObj2.addParameter(name='password', value='mst2010vhf', format='str')
# procUnitConfObj2.addParameter(name='localfolder', value=figures_path, format='str')
# procUnitConfObj2.addParameter(name='remotefolder', value=remotefolder, format='str')
# procUnitConfObj2.addParameter(name='ext', value='.png', format='str')
# procUnitConfObj2.addParameter(name='period', value='60', format='int')
# procUnitConfObj2.addParameter(name='protocol', value='ftp', format='str')

#######################################################################
############### UNIDAD DE ESCRITURA ###################################
#######################################################################

#opObj11 = procUnitConfObjSousySpectra.addOperation(name='SpectraWriter', optype='other')
#opObj11.addParameter(name='path', value=wr_path)
#opObj11.addParameter(name='blocksPerFile', value='50', format='int')
print "Escribiendo el archivo XML"
controllerObj.writeXml(filename)
print "Leyendo el archivo XML"
controllerObj.readXml(filename)

controllerObj.createObjects()
controllerObj.connectObjects()
controllerObj.run()
