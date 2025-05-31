import os
import pyfiglet
from db.DBKon import Koneksi as conn
from db.DBKon import conn
from TampilkanMenu.MenuASN import PanelAparat
def LoginAparat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Login ASN"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'asn'", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login berhasil!")
        PanelAparat()
    else: 
        print("Login gagal! Anda Bukan ASN Dari System.")
        cursor.close()
        conn.close()
        input("Tekan Enter untuk mencoba ulang...")
        LoginAparat()