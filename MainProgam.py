import os
import pyfiglet
from FormLogin.LoginAwal import LOGIN
import time

def animasi_teks(teks, delay=0.05):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print()  

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    judul = pyfiglet.figlet_format("SIMANDESA")
    for baris in judul.splitlines():
        animasi_teks(baris, delay=0.01)
    animasi_teks("Sistem Informasi Desa", delay=0.04)
    animasi_teks("Selamat Datang di Sistem Informasi Desa Suci", delay=0.04)
    animasi_teks("Dibuat Dengan Cinta Oleh Kelompok 3", delay=0.04)
    animasi_teks("Silakan login untuk melanjutkan...", delay=0.04)
    time.sleep(2)
    LOGIN()

main()
