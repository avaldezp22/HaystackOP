class VoltageReader():
    isConfig =False
    self.profileIndex = 2**32 -1
    def __init__(self):
        pass

    def set_kwargs(self):
        for key, value in kwargs.items():
        setattr(self, key, value)
    def searchFilesOffline(self,**kwargs):
        if walk:
            folders= self.find_folders()
        else:
            folders = path.split(",")
        return self.find_files()
# Aqui en setup se tiene los parametros de
# dataOut, path, blocksPerfile
# profilesPerBlock=64 , set= None, ext= None
# datatype
    def readFirstHeader(self):
        self.getBlockDimension()

    def setNextFile(self):
        while True:
            if self.onlie:
                newFile = self.setNextFileOnline()
            else:
                newFile = self.setNextFileOffline()
        self.readFirstHeader()

    def setNextFileOffline(self):
        try:
            filename=  next(self.filenameList)
            self.fileIndex+=1
        except StopIteration:
            self.flaNoMoreFiles = 1
            return 0
        self.filename = filename
        self.flagIsNewFile =1


    def setup(self,**kwargs):
        self.set_kwargs(**kwargs)
        if not self.ext.startswith('.'):
            self.ext = '.{}'.format(self.ext)
        if self.server is not None:
            pass
        else:
            self.server = None
            if self.path ==None:
                pass
            if self.online:
                fullpath = self.searchFilesOnline(**kwargs)
            else:
                self.filenameList= self.searchFilesOffline(**kwags)
            self.setNextFile()
        return

    def __hasNotDataInBuffer(self):
        if self.profileIndex >= self.processingHeaderObj.profilesPerBlock * self.nTxs:
            return 1

        return 0

    def readBlock(self):

        junk = numpy.fromfile(self.fp, self.dtype, self.blocksize)
        junk = junk.reshape((self.processingHeaderObj.profilesPerBlock,
                                 self.processingHeaderObj.nHeights, self.systemHeaderObj.nChannels))
        self.datablock = junk['real'] + junk['imag'] * 1j

        self.profileIndex = 0

        self.flagIsNewFile = 0
        self.flagIsNewBlock = 1

        self.nTotalBlocks += 1
        self.nReadBlocks += 1

        return 1

    def readNextBlock(self):
        while True:
            self.__setNewBLock()
            if not (self.readBlock()):
                return 0
            break
        return 1


    def getBasicHeader(self):
        self.dataOut.utctime = self.basicHeaderObj.utc + self.basicHeaderObj.miliSecond / \
            1000. + self.profileIndex * self.radarControllerHeaderObj.ippSeconds

        self.dataOut.flagDiscontinuousBlock = self.flagDiscontinuousBlock

        self.dataOut.timeZone = self.basicHeaderObj.timeZone

        self.dataOut.dstFlag = self.basicHeaderObj.dstFlag

        self.dataOut.errorCount = self.basicHeaderObj.errorCount

        self.dataOut.useLocalTime = self.basicHeaderObj.useLocalTime

        self.dataOut.ippSeconds = self.radarControllerHeaderObj.ippSeconds / self.nTxs

    def getFirstHeader(self):
        self.getBasicHeader()

    def getData(self): ### metodo prodpio de VoltageReader
        check:
        self.flaNoMoreFiles
            self.dataOut.flagNodata= True
        self.flagDiscontinuousBlock=0
        self.flagIsNewBlock       = 0
        if self.__hasNotDataInBuffer():  # aqui es verdad
            if not(self.readNextBlock()): # return 1 y por eso el if not salta  a getBasic Header
                return 0
            self.getFirstHeader() # atributo
            self.reshapeData() # nTxx1 =1 return , n

        if not self.getByBlock:
            self.dataOut.flagDataAsBlock = False
            self.dataOut.data = self.datablock[:, self.profileIndex, :]
            self.dataOut.profileIndex = self.profileIndex

            self.profileIndex += 1
        else:
            pass
        self.getBasicHeader()
        self.dataOut.realtime = self.searchFilesOnline

        return self.dataOut.data

    def run(self): # metodo propio
        if not(self.isConfig):
            self.setup(**kwargs)
        self.isConfig = True
        if self.server is None:
            self.getData()
        else:
            self.getFromServer()
