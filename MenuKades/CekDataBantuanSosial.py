import os
import pyfiglet
from Databasehelper.DBKon import conn
from TampilkanMenu.MenuKades import PanelKades
def CekDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Cek Data Bantuan Sosial"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bantuan_sosial")
    result = cursor.fetchall()
    if result:
        print("Data Bantuan Sosial:")
        for row in result:
            print(f"Nama: {row[0]}, NIK: {row[1]}, Jenis Bantuan: {row[2]}, Tanggal: {row[3]}")
    else:
        print("Tidak ada data bantuan sosial.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu KADES...")
    PanelKades()