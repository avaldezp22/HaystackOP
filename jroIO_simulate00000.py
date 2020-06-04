
####jroIO_voltage.py
class VoltageReader (  JRODataReader,ProcessingUnit):
    __init__(self):
    createObjByDefault(self):
    __hasNotDataInBuffer(self):
    getBlockDimension(self):
    readBlock(self):
    getFirstHeader(self):
    reshapeData(self):
     readFirstHeaderFromServer(self):
    #-------------------ojo aqui method get------------
    getFromServer(self):
    getData(self):

######jroIO_base.py
class Reader(object):

    getAllowrdArgs(self)
    set_kwargs(self,**kwargs)
    find_folders(self,path,startDate,endDate,folderfmt,last=False)
    find_files(self,folders,ext,filefmt,start)
    searchFilesOffLine()
        find_folders()
        find_files()
    searchFilesOnLine()
        find_folders()
        find_files()
    setNextFile()
        online:
            setNextFileOnline
        offline:
            setNextFileOffline
        readFirstHeader
    setNextFileOnline()
        checkForRealPath
    setNextFileOffline()
    isDateTimeInRange()
    #-------------------------- EMPTY    -------------------------------
    verifyFile(self,filename) ---empty
    checkForRealPath(self,nexFile,nexDay) ------empty
    readFirstHeader(self) ------- empty
    run()


########
class JRODataReader(Reader):
    getDtypeWidth()
    checkForRealPath(self,nextFile,nextDay)
    __waitNewBlock(self)
    waitDataBlock(pointer_location,blocksize=None)
    __setNewBlock()
        self.setNextFile()  ---Reader
        self.__waintNewBlock()
    readNextBlock()
        self.__setNewBlock()
        self.readBlock()
        self.getBasicHeader()
    readFirstHeader()
        self.getBlockDimension() #####recien se crea en el voltageReader
    verifyFile()
        waitDataBlock()
        isDateTimeInRange
    findDatafiles()
    setup(self,**kwargs)
        set_kwargs()
        if server is None:
            pass
        else:
            if online:
                self.searchFilesOnLine
            else:
                self.searchFilesOffLine

    getBasicHeader(self)
    #--------------------------------------------
    run()
        if not(self.isConfig):
            self.setup(**kwargs)
            self.isConfig = True
        if self.server is None:
            self.getData()
        else:
            self.getFromServer()
    #----------------------------------------------
    #---------   Not Implemented Error-------------------------
    getFirstHeader()
    getData()
    hasNotDataInBuffer()
    readBlock()
    isEndProces()
        return self.flagNoMoreFiles
    printReadBlocks()
    printTotalBlocks()
    printNumberOfBlock()
    printInfo()
