#!/usr/bin/env python
#LINUX
#bash: export WRADLIB_DATA=/path/to/wradlib-data
import os
import matplotlib.pyplot as pl
import wradlib as wrl
import numpy as np
pl.switch_backend("TKAgg")
#filename = wrl.util.get_wradlib_data_file('dx/raa00-dx_10908-0806021655-fbg---bin.gz')


validFilelist = []
path= '/home/alex/Downloads/2019-12-29/'
fileList= os.listdir(path)
for thisFile in fileList:
    if (os.path.splitext(thisFile)[0][-4:] != 'dBuZ'):
        continue
    validFilelist.append(thisFile)
    validFilelist.sort()

#print (validFilelist)
for thisFile in validFilelist:
    print(thisFile)	
    fpath = path+thisFile
    f = wrl.util.get_wradlib_data_file(fpath)
    fcontent = wrl.io.read_rainbow(f)
    #print (fcontent)
    #print(sfcontent['volume']

    #Get azimuth data
    azi = fcontent['volume']['scan']['slice']['slicedata']['rayinfo']['data']
    azidepth = float(fcontent['volume']['scan']['slice']['slicedata']['rayinfo']['@depth'])
    azirange = float(fcontent['volume']['scan']['slice']['slicedata']['rayinfo']['@rays'])
    azires = float(fcontent['volume']['scan']['slice']['anglestep'])
    azi = (azi * azirange / 2**azidepth) * azires

    # Create range array
    stoprange = float(fcontent['volume']['scan']['slice']['stoprange'])
    rangestep = float(fcontent['volume']['scan']['slice']['rangestep'])
    r = np.arange(0, stoprange, rangestep)

    # GET reflectivity data#print (fcontent)
    #print(sfcontent['volume']
    data = fcontent['volume']['scan']['slice']['slicedata']['rawdata']['data']
    datadepth = float(fcontent['volume']['scan']['slice']['slicedata']['rawdata']['@depth'])
    datamin = float(fcontent['volume']['scan']['slice']['slicedata']['rawdata']['@min'])
    datamax = float(fcontent['volume']['scan']['slice']['slicedata']['rawdata']['@max'])
    data = datamin + data * (datamax - datamin) / 2 ** datadepth

    #print(fcontent['volume']['sensorinfo'])
    #print("ESPACIO")
    #print(data)

    #GET ANNOTATION data
    unit = fcontent['volume']['scan']['slice']['slicedata']['rawdata']['@type']
    time = fcontent['volume']['scan']['slice']['slicedata']['@time']
    date = fcontent['volume']['scan']['slice']['slicedata']['@date']
    lon = fcontent['volume']['sensorinfo']['lon']
    lat = fcontent['volume']['sensorinfo']['lat']
    sensortype = fcontent['volume']['sensorinfo']['@type']
    sensorname = fcontent['volume']['sensorinfo']['@name']

    # PLOT DATA WITH ANNOTATION
    fig = pl.figure(figsize=(8,8))
    cgax, pm = wrl.vis.plot_ppi(data, r=r, az=azi, fig=fig, proj='cg')

    title = '{0} {1} {2} {3}\n{4}E {5}N'.format(sensortype, sensorname, date,time, lon, lat)
    caax = cgax.parasites[0]
    t = pl.title(title, fontsize=12)
    t.set_y(1.1)
    cbar = pl.gcf().colorbar(pm, pad=0.075)
    caax.set_xlabel('x_range [km]')
    caax.set_ylabel('y_range [km]')
    pl.text(1.0, 1.05, 'azimuth', transform=caax.transAxes, va='bottom',
            ha='right')
    cbar.set_label('reflectivity [' + unit + ']')
    pl.show()

    #print ("FIN")
    #import time
    #time.sleep(2)
    #pl.close()
    # stop here
    #print(fcontent['data'])
    #data, metadata = wrl.io.read_dx(filename)
    #ax, pm = wrl.vis.plot_ppi(data) # simple diagnostic plot
    #cbar = pl.colorbar(pm, shrink=0.75)
