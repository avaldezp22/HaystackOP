#!python
''''''
import os,sys
from schainpy.controller import Project

id= '100'
filename ='Test_COPPERBALL'
desc     ='Adquisition system Copperball test'

controllerObj = Project()
controllerObj.setup(id=id , name=filename , description=desc)

##########  NOS ENFOCAMOS PRINCIPALMENTE EN RACP Y COPPERBALL #########
#######################################################################
################# UNIDAD ESCRITURA, CONFIGURACION     #################
#######################################################################
racpfile='/home/alex/Downloads/dia_mod.racp'
acq_type='copperball'

writeUnitConfObj = controllerObj.addWriteUnit(datatype='Hdf5Writer',
                                              racpfile=racpfile,
                                              acq_type=acq_type
                                             )

#######################################################################
######################## PARAMETERSPROC################################
################ OPERACIONES DOMINIO DEL TIEMPO   #####################
#######################################################################

procUnitConfObj0 = controllerObj.addProcUnit(datatype='ParametersProc', inputId=writeUnitConfObj.getId())

#######################################################################
################### OPERACION DE ESCRITURA  ###########################
#######################################################################
path='/home/alex/Downloads/data'

opObj21 = procUnitConfObj0.addOperation(name='ParameterWriter', optype='external')
opObj21.addParameter(name='path', value=path)
opObj21.addParameter(name='blocksPerFile', value='10', format='int')
opObj21.addParameter(name='metadataList',value='utctime',format='list')
opObj21.addParameter(name='dataList',value='data',format='list')

print ("Escribiendo el archivo XML")
print ("Leyendo el archivo XML")

controllerObj.start()

