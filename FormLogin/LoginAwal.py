import os
import pyfiglet
from FormLogin.LoginAdmin import LoginAdmin
from FormLogin.LoginASN import LoginAparat
from FormLogin.LoginRW import LoginRW
def LOGIN():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("SIMANDESA"))
    print("Silahkan Login Sebagai:")
    print("1.Admin")
    print("2.Aparat")
    print("3.RW")
    print("4.Exit")
    pil = input("Pilih Menu:" )
    if pil == "1":
        LoginAdmin()
    elif pil == "2":
        LoginAparat()
    elif pil == "3":
        LoginRW()
    elif pil == "4":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        LOGIN()