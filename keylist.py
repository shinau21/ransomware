import os

keylist = []
for p, d, f in os.walk('pub'):
    for name in f:
        keylist.append(name)
print(keylist)