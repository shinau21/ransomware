import os

keylist = []
ext = []
for p, d, f in os.walk('pub'):
    for name in f:
        keylist.append(name)
        ext.append(name.split('.')[1])
print(keylist)
#print(ext)