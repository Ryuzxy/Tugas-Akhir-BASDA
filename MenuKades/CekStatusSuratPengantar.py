import os
import pyfiglet
from Databasehelper.DBKon import conn
from TampilkanMenu.MenuKades import PanelKades
def CekStatusSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Cek Status Surat Pengantar"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_pengantar")
    result = cursor.fetchall()
    if result:
        print("Data Surat Pengantar:")
        for row in result:
            print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}, Status: {row[4]}")
    else:
        print("Tidak ada data surat pengantar.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu KADES...")
    PanelKades()
