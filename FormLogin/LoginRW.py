import os
import pyfiglet
from db.DBKon import conn
from TampilkanMenu.MenuRW import PanelRW
def LoginRW():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("SIMANDESA"))
    print("=====================   LOGIN RW   =====================")

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'rw'", (username, password))
        result = cursor.fetchone()

        if result:
            print("Login berhasil!")
            cursor.close()
            PanelRW(username) 
        else: 
            print("Login gagal! Anda Bukan RW Dari System.")
            cursor.close()
            input("Tekan Enter untuk mencoba ulang...")
            LoginRW()
    except Exception as e:
        print("Terjadi kesalahan saat login:", e)
        input("Tekan Enter untuk keluar...")