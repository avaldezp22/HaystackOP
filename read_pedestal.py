import h5py
path="/home/soporte/Downloads/pedestal/PE20193581577199362.hdf5"


with h5py.File(path,'r') as f:
    #List all groups
    print("keys: %s"%f.keys())
    a_group_key= list(f.keys())[0]
    # GET THE data
    data = list(f[a_group_key])
    print(data[0])
    print(data[1])
    print(data[2])
