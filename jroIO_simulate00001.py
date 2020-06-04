############################################
########### VoltageReader ##################
############################################
#---------------------------------
## Leer datos del voltage de archivos en formato rawdata(.r).
## lectura de los datos siempre se realiza por bloques.
## Datos leidos son almacenados en un buffer. perfiles*alturas*canales
## Contiene instancias(objetos) de los clases:

    * BasicHeader
    * SystemHeader
    * RadarControllerHeader
    * voltage


# Los 3 primeros  se usan para almacenar informacion
# de la cabecera de datos(metadata)
# El cuarto para obtener y almacenar un pefil de datos desde el buffer
# cada vez que se ejecuta el meodo de "getdata"

# dpath
# startTime , endTime
# readerObj= VoltageReader() # SimulateReader()
# readerObj.setup(dpath,startTime,endTime,**parametros)
#  while (True):
#      profile = readerObj.getData()
#      print (profile)
#      print (readerObj.datablock)
#      if readerObj.flagNoMoreFiles:
#           break

class VoltageReader(JRODataReader,ProcessingUnit):

    __init__(self):

        self.dataOut                = Voltage()

    createObjByDefault(self):
        dataObj = Voltage()

        return dataObj
    __hasNotDataInBuffer(self):
        if self.profileIndex >=self.processingHeaderObj.profilesPerBlock * self.nTxs:
            return 1
        return 0

    getBlockDimension()

    readBlock()
        waitDataBlock

    getFirstHeader()
        getBasicHeader() ---- JRODataReader

    reshapeData()

    readFirstHeaderFromServer(self):
        getFirstHeader
        getBlockDimension
    getFromServer(self):
        readFirstHeaderFromServer

    getData(self):
        if hasNotDataInBuffer
            if not readNextBlock --- JRODataReader
                return
            getFirstHeader ----- check
            reshapeData    ----- check
        if not self.getByBlock:

        else:
            readNextBlock()
            getFirstHeader
            reshapeData
        self.getBasicHeader()

        return self.dataOut.data
