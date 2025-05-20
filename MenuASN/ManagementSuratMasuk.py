import os
import pyfiglet
from Databasehelper.DBKon import conn
from ManagementSuratMasuk.TambahSuratMasuk import TambahSuratMasuk
from ManagementSuratMasuk.HapusOrUbahSuratMasuk import HapusOrUbahSuratMasuk
from ManagementSuratMasuk.TampilkanSuratMasuk import TampilkanSuratMasuk    
from ManagementSuratMasuk.TampilkanSuratPengantar import TampilkanSuratPengantar
from ManagementSuratMasuk.ApproveSuratPengantar import ApproveSuratPengantar    
from TampilkanMenu.MenuASN import PanelAparat
def ManagementSuratMasuk():
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("Management Surat Masuk"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Surat Masuk")
    print("2.Hapus/Ubah Surat Masuk")
    print("3.Tampilkan Surat Masuk")
    print("4.Tampilkan Surat Pengantar")
    print("5.Approve Surat Pengantar")
    print("6.Kembali Ke Menu ASBA")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratMasuk()
    elif pil == "2":
        HapusOrUbahSuratMasuk()
    elif pil == "3":
        TampilkanSuratMasuk()
    elif pil == "4":
        TampilkanSuratPengantar()
    elif pil == "5":
        ApproveSuratPengantar()
    elif pil == "6":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSuratMasuk()