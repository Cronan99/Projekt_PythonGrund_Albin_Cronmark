import pickle

def loadfile(file):
    with open(file, "rb") as f:
        return pickle.load(f)
    
def savefile(list, file):
    with open(file, "wb") as f:
        pickle.dump(list, f)