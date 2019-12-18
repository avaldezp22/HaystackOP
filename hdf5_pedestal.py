import h5py
import os
import time
import numpy


path="/home/soporte/Downloads"
ext=".hdf5"
optchar="P"
metaoptchar= "PE"
dtype = [('arrayName', 'S20'),('nDimensions', 'i'), ('dim2', 'i'), ('dim1', 'i'),('dim0', 'i')]

def putMetadata():
    print ("C logra")
    fp = createMetadataFile()
    writeMetadata(fp)
    fp.close()

def createMetadataFile():
    timetuple = time.localtime()
    fullpath = path + ("/" if path[-1]!="/" else "")
    print (timetuple)

    if not os.path.exists(fullpath):
        os.mkdir(fullpath)

    filex ="%s%4.4d%3.3d%s"%(metaoptchar, timetuple.tm_year,timetuple.tm_yday,ext)
    filename = os.path.join(fullpath,filex)
    metafile=filex
    fp = h5py.File(filename,'w')
    print (filex)
    return fp

def writeMetadata(fp):
    grp = fp.create_group("Metadata")
    grp.create_dataset('array dimensions',data = self.tableDim,dtype= dtype,compression='gzip')
    for i in range(len(metadataList)):
        # try to compress
        data = getattr(dataOut_pedestal,metadaList[i])
        if hasttr(data,'len') and type(data):
            grp.create_dataset(metadataList[i])
        else:
            grp.create_dataset(medataList[i],data)

#data_pedestal  (ang_elev, ang_azi)
def setup(path, data_pedestal,tiempo):
    print "avp"

def run():
    print "abcdef"

#createMetadataFile()
putMetadata()
