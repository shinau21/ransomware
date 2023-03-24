import os
import random
import string
from time import sleep
from cryptography.fernet import Fernet as xf
from Crypto.PublicKey import RSA

state = False
while (state!=True):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    kpx = RSA.generate(2048)
    pbk = kpx.publickey().exportKey()
    fpbk = open(name+".pem","wb")
    fpbk.write(pbk)
    fpbk.close()
    pvk = kpx.exportKey()
    fpvk = open(name+"-priv.pem","wb")
    fpvk.write(pvk)
    fpvk.close()
    x = input("Generate Lagi? (Y/N)")
    if (x == 'Y'):
        state = False
    elif (x == 'N'):
        state = True
    else:
        print("Only Y or N")