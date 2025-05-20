import os
import pyfiglet
from FormLogin.LoginAdmin import LoginAdmin
from FormLogin.LoginASN import LoginAparat
from FormLogin.LoginKades import LoginKades
def LOGIN():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang di SIMANDESA"))
    print("Silahkan Login Sebagai:")
    print("1.Admin")
    print("2.Aparat")
    print("3.Kades")
    print("4.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        LoginAdmin()
    elif pil == "2":
        LoginAparat()
    elif pil == "3":
        LoginKades()
    elif pil == "4":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        LOGIN()