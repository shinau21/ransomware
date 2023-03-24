import os
from time import sleep
from cryptography.fernet import Fernet as xf
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def defense(target):
    for p, d, f in os.walk(target):
        for name in f:
            if name.endswith((".itsec")):
                try:
                    #encrypt(os.path.join(p, name),RSA.importKey(pbk))

                    with open(p + name, "rb") as mfile:
                        newFile = p + os.path.splitext(name)[0]
                        file_in = open(newFile, "wb")

                        private_key = RSA.import_key(open("private.pem").read())

                        enc_session_key, nonce, tag, ciphertext = [ mfile.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
                        mfile.close()

                        # Decrypt the session key with the private RSA key
                        cipher_rsa = PKCS1_OAEP.new(private_key)
                        session_key = cipher_rsa.decrypt(enc_session_key)

                        # Decrypt the data with the AES session key
                        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
                        file_in.write(data)
                        file_in.close()
                        mfile.close()
                        os.remove(os.path.join(p, name))
                except:
                    continue
                try:
                    os.remove(os.path.join(p,"_readme.txt"))
                except:
                    status = "All Files has been Decrypted"

if __name__ == '__main__':
    t0 = os.environ["USERPROFILE"] + "\\Videos\\"
    defense(t0)