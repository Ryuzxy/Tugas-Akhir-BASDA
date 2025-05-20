import os
import pyfiglet
from Databasehelper.DBKon import conn
from TampilkanMenu.MenuASN import ManagementSuratMasuk
def TambahSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Masuk"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    pengirim = input("Masukkan nama pengirim: ")
    perihal = input("Masukkan perihal surat: ")       
    cursor = conn.cursor()
    cursor.execute("INSERT INTO surat_masuk (nomor_surat, tanggal, pengirim, perihal) VALUES (%s, %s, %s, %s)", (nomor_surat, tanggal, pengirim, perihal))
    conn.commit()
    cursor.close()       
    print("Surat berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratMasuk()