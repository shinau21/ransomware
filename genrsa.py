import os
import random
import string
import base64
from time import sleep
from cryptography.fernet import Fernet as xf
from Crypto.PublicKey import RSA

state = False
while (state!=True):
    y = input("Nama Extensi : ")
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    enc_priv = base64.b64encode(name.encode('utf-8'))
    kpx = RSA.generate(2048)
    pbk = kpx.publickey().exportKey()
    fpbk = open("pub/"+name+"."+y+".pem","wb")
    fpbk.write(pbk)
    fpbk.close()
    pvk = kpx.exportKey()
    fpvk = open("priv/"+str(enc_priv.decode('utf-8'))+".pem","wb")
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