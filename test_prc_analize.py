import os
import numpy as np
import prc_analyze
import glob
from argparse import ArgumentParser


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def codigo(args):
    code_list=[]
    PATH="/home/alex/digital_rf/python/examples/sounder/waveforms/"
    os.chdir(PATH)
    for file in glob.glob("*.bin"):
        code_list.append(file)
    print code_list
    raw_input("<Press enter>")
    codefile =PATH+code_list[args.code]
    path,filename = os.path.split(codefile) 
    code_vector = np.fromfile(codefile,dtype=np.complex64)
    print "CODE ACTIVATE %d"%args.code,filename
    print "code_Tx",code_vector.shape
    print code_vector[0:args.point]
    plot_draw= not (args.show)
    prc_analyze.plot_cts(code_vector[0:args.point],plot_abs=args.abso,plot_draw=plot_draw,plot_show=args.show)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-code', '--code', type=int, default=0,
             help='''Number of code. (default: %(default)s)''',
             )

    parser.add_argument('-point', '--point', type=int, default=100,
             help='''Number of points to plot . (default: %(default)s)''',
             )

    parser.add_argument('-abso', '--abso', type=str2bool, default=False,
        help='''Show abs of the signal.''',
    )

    parser.add_argument('-show', '--show', type=str2bool, default=False,
        help='''Show abs of the signal.''',
    )
    

    args = parser.parse_args()

    codigo(args)

    
    
