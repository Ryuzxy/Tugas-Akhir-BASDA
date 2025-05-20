import os
import pyfiglet
from MenuKades.TambahSuratPengantar import TambahSuratPengantar
from MenuKades.CekStatusSuratPengantar import CekStatusSuratPengantar
from MenuKades.CekDataBantuanSosial import CekDataBantuanSosial
def PanelKades():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang Kades"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Surat Pengantar")
    print("2.Cek Status Surat Pengantar")
    print("3.Cek Data Bantuan Sosial")
    print("4.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratPengantar()
    elif pil == "2":
        CekStatusSuratPengantar()
    elif pil == "3":
        CekDataBantuanSosial()
    elif pil == "4":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:   
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelKades()