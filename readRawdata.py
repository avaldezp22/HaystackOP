import datetime

from schainpy.model import *

path='/home/alex/Downloads'
rawdataObj = VoltageReader()
'''
while not(rawdataObj.flagNoMoreFiles):
    if not (rawdataObj.isConfig):
        rawdataObj.setup(path = path,
               startDate = datetime.date(2015,1,1),
               endDate = datetime.date(2015,12,25),
               startTime = datetime.time(0,0,0),
               endTime = datetime.time(23,59,59),
               online=0,
               walk =False)
        rawdataObj.isConfig =True

    if rawdataObj.server is None:
        rawdataObj.getData()
    else:
        rawdataObj.getFromServer()

    print (rawdataObj.dataOut.datatime)
    print (rawdataObj.dataOut.data)
    import time
    time.sleep(1)

print ('task completed successfully')
'''
