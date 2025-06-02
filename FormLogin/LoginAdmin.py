import pyfiglet
import os
from db.DBKon import conn
from TampilkanMenu.MenuAdmin import PanelAdmin
def LoginAdmin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("SIMANDESA"))
    print("====================   LOGIN ADMIN   ====================")

    username = input("\nMasukkan username : ")
    password = input("Masukkan password : ")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'admin'", (username, password))
        result = cursor.fetchone()

        if result:
            print("Login berhasil!")
            cursor.close()
            PanelAdmin(username)  # kirim username ke PanelAdmin
        else: 
            print("Login gagal! Anda Bukan Admin Dari System.")
            cursor.close()
            input("Tekan Enter untuk mencoba ulang...")
            LoginAdmin()
    except Exception as e:
        print("Terjadi kesalahan saat login:", e)
        input("Tekan Enter untuk keluar...")