#!python
import numpy as np
from argparse import ArgumentParser
import prc_analyze

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



def wave_fft(args):
    if args.file is None:
        print "Write a path with a filename to read numpy.fromfile"
    else:
        file_w = args.file
    wave_f= np.fromfile(file_w,dtype=np.complex64)
    fft = np.fft.fft(wave_f)
    fft = np.fft.fftshift(fft)
    fft = fft / np.max(np.abs(fft))
    #fft = np.abs(fft)**2.0
    plot_draw= not (args.show)
    prc_analyze.plot_cts(fft,plot_abs=args.abso,plot_draw=plot_draw,plot_show=args.show)
    

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-file", "--file",dest="file", action="store", type=str,default= None,
                                          help="Insert file.")

    parser.add_argument('-code', '--code', type=int, default=0,
             help='''Number of code. (default: %(default)s)''',
             )

    parser.add_argument('-abso', '--abso', type=str2bool, default=False,
        help='''Show abs of the signal.''',
    )

    parser.add_argument('-show', '--show', type=str2bool, default=False,
        help='''Show abs of the signal.''',
    )
    

    args = parser.parse_args()

    wave_fft(args)

    
        
