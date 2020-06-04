## atom: apm install symbols-tree-view


class VoltageReader:
    def readFirstHeader(self):
        self.basicHeaderObj.read(self.fp)
        self.systemHeaderObj.read(self.fp)
        self.radarControllerHeaderObj.read(self.fp)
        self.processingHeaderObj.read(self.fp)
        self.firstHeaderSize = self.basicHeaderObj.size
        self.getBlockDimension()

    def searchFilesOffLine(self):  # Este metodo esta declarado en
        if walk:
            foldes= self.find_folders()
        else:
            folders=  path.split(',')
        return self.find_files()

    def setNextFile(self):
        while True:
            if self.online:
                newFile= self.setNextFileOnline()
            else:
                newFile= self.setNextFileOffline()
        self.readFirstHeader()

    def setup(self,**kwargs): # Declarado en el JRODataReader
        self.set_kwargs(**kwargs)
        if self.server is not None:
            pass
        else:
            self.server = None
            if self.path == None:
                pass
            if self.online:
                pass
            else:
                    self.filenameList = self.searchFilesOffLine(self.path,
                                                                self.startDate,
                                                                self.endDate,
                                                                self.expLabel,
                                                                self.ext,
                                                                self.walk,
                                                                self.filefmt,
                                                                self.folderfmt)
            self.setNextFile()
        return


    def __hasNotDataInBuffer(self):

        if self.profileIndex >= self.processingHeaderObj.profilesPerBlock * self.nTxs:
            return 1

        return 0

    def getData(self):
        if self.__hasNotDataInBuffer(): # SI ES MENO QUE LA CANTIDAD DE PROFILEPERBLOCK RETURN FALSE
            if not(self.readNextBLock()):
                return 0
            self.getFirstHeader()
            self.reshapeData()
        if not self.getByBlock:
            pass
        else:
            pass
        self.getBasicHeader()
        return self.dataOut.data



    def run():                          #    Este run esta declarado en Reader y JRODataReader pero no en VoltageReader
        if not(self.isConfig):          #
            self.setup(**kwargs)        #
            self.isConfig = True
        if self.server is None:
            self.getData()
        else:
            self.getFromServer()
