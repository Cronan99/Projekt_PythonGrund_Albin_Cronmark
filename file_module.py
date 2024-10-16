import pickle

"""Functions below use pickle to save and load files as binary data"""
def loadfile(file):
    with open(file, "rb") as f:
        return pickle.load(f)
    
def savefile(list, file):
    with open(file, "wb") as f:
        pickle.dump(list, f)