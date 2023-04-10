import os
import random
import string
import hashlib
from time import sleep
from cryptography.fernet import Fernet as xf
from Crypto.PublicKey import RSA

state = False
while (state!=True):
    y = input("Nama Extensi : ")
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(5))
    enc_priv = hashlib.sha1(name.encode('utf-8')).hexdigest()
    kpx = RSA.generate(2048)
    pbk = kpx.publickey().exportKey()
    fpbk = open("pub/"+name+"."+y+".pem","wb")
    fpbk.write(pbk)
    fpbk.close()
    pvk = kpx.exportKey()
    fpvk = open("priv/"+str(enc_priv)+".pem","wb")
    fpvk.write(pvk)
    fpvk.close()
    x = input("Generate Lagi? (Y/N)")
    if (x == 'Y'):
        state = False
    elif (x == 'N'):
        state = True
    else:
        print("Only Y or N")
        break