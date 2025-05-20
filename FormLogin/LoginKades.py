import os
import pyfiglet
from db.DBKon import Koneksi as conn
from TampilkanMenu.MenuKades import PanelKades
def LoginKades():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Login Kades"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'KADES'", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login berhasil!")
        PanelKades()
    else: 
        print("Login gagal! Anda Bukan Kades Dari System.")
        cursor.close()
        conn.close()
        input("Tekan Enter untuk mencoba ulang...")
        LoginKades()