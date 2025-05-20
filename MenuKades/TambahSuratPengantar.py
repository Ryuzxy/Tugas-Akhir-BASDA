import os
import pyfiglet
from db.DBKon import Koneksi as conn
from TampilkanMenu.MenuKades import PanelKades
def TambahSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Pengantar"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    pengirim = input("Masukkan nama pengirim: ")
    perihal = input("Masukkan perihal surat: ")       
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Surat_pengantar (Nomor_surat, Tanggal, Pengirim, Perihal) VALUES (%s, %s, %s, %s)", (nomor_surat, tanggal, pengirim, perihal))
    conn.commit()
    cursor.close()       
    print("Surat pengantar berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu KADES...")
    PanelKades()