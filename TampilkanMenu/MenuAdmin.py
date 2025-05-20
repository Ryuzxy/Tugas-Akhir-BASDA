import os
import pyfiglet
from MenuAdmin.TambahDataLoginUser import TambahDataLoginUser
from MenuAdmin.HapusOrUbahDataLoginUser import HapusOrUbahDataLoginUser
from MenuAdmin.TampilkanDataLoginUser import TampilkanDataLoginUser
from MenuAdmin.TambahDataInventaris import TambahDataInventaris
from MenuAdmin.HapusOrUbahDataInventaris import HapusOrUbahDataInventaris
from MenuAdmin.TampilkanDataInventaris import TampilkanDataInventaris
def PanelAdmin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang Admin"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Data Login User")
    print("2.Hapus/Ubah Data Login User")
    print("3.Tampilkan Data Login User")
    print("4.Tambah Data Inventaris Desa")
    print("5.Hapus/Ubah Data Inventaris Desa")
    print("6.Tampilkan Data Inventaris Desa")
    print("7.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataLoginUser()
    elif pil == "2":
        HapusOrUbahDataLoginUser()
    elif pil == "3":
        TampilkanDataLoginUser()
    elif pil == "4":
        TambahDataInventaris()
    elif pil == "5":
        HapusOrUbahDataInventaris()
    elif pil == "6":
        TampilkanDataInventaris()
    elif pil == "7":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelAdmin()
