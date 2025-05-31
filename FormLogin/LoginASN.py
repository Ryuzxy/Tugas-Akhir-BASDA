import os
import pyfiglet
from db.DBKon import conn
from TampilkanMenu.MenuASN import PanelAparat
def LoginAparat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Login ASN"))

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'aparat'", (username, password))
        result = cursor.fetchone()

        if result:
            print("Login berhasil!")
            cursor.close()
            PanelAparat(username)  # kirim username ke PanelAparat
        else: 
            print("Login gagal! Anda Bukan ASN Dari System.")
            cursor.close()
            input("Tekan Enter untuk mencoba ulang...")
            LoginAparat()
    except Exception as e:
        print("Terjadi kesalahan saat login:", e)
        input("Tekan Enter untuk keluar...")