import pickle

l=[10, 20, 40, 30]

#dump()
file=open("writedata.txt", "wb")
pickle.dump(l, file)
file.close()

#load()
file=open("writedata.txt", "rb")
l=pickle.load(file)
print(l)