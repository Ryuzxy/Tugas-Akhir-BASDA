import os
import pyfiglet
from Databasehelper.DBKon import conn
from MenuASN import ManagementSuratMasuk
from MenuASN import ManagementSuratKeluar
from MenuASN import ManagementDataPenduduk
from MenuASN import ManagementDataBantuanSosial
from MenuASN import LaporanBulanan
def PanelAparat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang ASDA"))
    print("Silahkan Pilih Menu:")
    print("1.Managemet Surat Masuk")
    print("2.Managemet Surat Keluar")
    print("3.Management Data Penduduk")
    print("4.Management Data Bantuan Sosial")
    print("5.Laporan Bulanan ")
    print("6.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementSuratMasuk()
    elif pil == "2":
        ManagementSuratKeluar()
    elif pil == "3":
        ManagementDataPenduduk()
    elif pil == "4":
        ManagementDataBantuanSosial()
    elif pil == "5":
        LaporanBulanan()
    elif pil == "6":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelAparat()