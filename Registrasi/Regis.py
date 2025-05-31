import os
import pyfiglet
from db.DBKon import conn
from TampilkanMenu.MenuAdmin import PanelAdmin
from TampilkanMenu.MenuASN import PanelAparat
from TampilkanMenu.MenuKades import PanelKades

def Regist():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Registrasi"))
    print("Pilih role yang ingin didaftarkan:")
    print("1. Admin")
    print("2. ASN")
    print("3. Kades")
    
    choice = input("Masukkan pilihan (1/2/3): ")
    
    if choice == '1':
        RegistrasiAdmin()
    elif choice == '2':
        RegistrasiASN()
    elif choice == '3':
        RegistrasiKades()
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        Regist()
def RegistrasiAdmin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Registrasi Admin"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, 'admin')", (username, password))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
        PanelAdmin()
    except Exception as e:
        print(f"Registrasi gagal! Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")

def RegistrasiASN():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Registrasi ASN"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, 'asn')", (username, password))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
        PanelAparat()
    except Exception as e:
        print(f"Registrasi gagal! Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")

def RegistrasiKades():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Registrasi Kades"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, 'kades')", (username, password))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
        PanelKades()
    except Exception as e:
        print(f"Registrasi gagal! Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    