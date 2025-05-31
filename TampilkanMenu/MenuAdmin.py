import os
import pyfiglet
from db.DBKon import Koneksi as conn
def PanelAdmin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang Admin"))
    print("Silahkan Pilih Menu:")
    print("1.Management Data Login User")
    print("2.Management Data Inventaris Desa")
    print("3.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementDataLoginUser()
    elif pil == "2":
        ManagementDataInventaris()
    elif pil == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Terima Kasih Telah Menggunakan System Kami"))  
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        print("Tekan Enter untuk kembali ke menu utama...")
        input()
        PanelAdmin()
def ManagementDataLoginUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Login User"))
    print("1.Tambah User")
    print("2.Hapus User")
    print("3.Lihat Data User")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahUser()
    elif pil == "2":
        HapusUser()
    elif pil == "3":
        LihatDataUser()
    elif pil == "4":
        PanelAdmin()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataLoginUser()
def TambahUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah User"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    role = input("Masukkan role (admin/asn/kades): ").lower()
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
        conn.commit()
        print("User berhasil ditambahkan!")
    except Exception as e:
        print(f"Error saat menambahkan user: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
    input("Tekan Enter untuk kembali...")
    ManagementDataLoginUser()
def HapusUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus User"))
    username = input("Masukkan username yang akan dihapus: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        conn.commit()
        if cursor.rowcount > 0:
            print("User berhasil dihapus!")
        else:
            print("User tidak ditemukan.")
    except Exception as e:
        print(f"Error saat menghapus user: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    
    input("Tekan Enter untuk kembali...")
    ManagementDataLoginUser()
def LihatDataUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data User"))
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        if users:
            print("Daftar User:")
            for user in users:
                print(f"Username: {user[1]}, Role: {user[3]}")
        else:
            print("Tidak ada user yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data user: {e}")
    finally:
        cursor.close()
        conn.close()
    
    input("Tekan Enter untuk kembali...")
    ManagementDataLoginUser()
def ManagementDataInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Inventaris Desa"))
    print("1.Tambah Inventaris")
    print("2.Hapus Inventaris")
    print("3.Lihat Data Inventaris")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahInventaris()
    elif pil == "2":
        HapusInventaris()
    elif pil == "3":
        LihatDataInventaris()
    elif pil == "4":
        PanelAdmin()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataInventaris()
def TambahInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Inventaris"))
    nama_inventaris = input("Masukkan nama inventaris: ")
    jumlah = input("Masukkan jumlah inventaris: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO inventaris (nama_inventaris, jumlah) VALUES (%s, %s)", (nama_inventaris, jumlah))
        conn.commit()
        print("Inventaris berhasil ditambahkan!")
    except Exception as e:
        print(f"Error saat menambahkan inventaris: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataInventaris()
def HapusInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Inventaris"))
    nama_inventaris = input("Masukkan nama inventaris yang akan dihapus: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM inventaris WHERE nama_inventaris = %s", (nama_inventaris,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Inventaris berhasil dihapus!")
        else:
            print("Inventaris tidak ditemukan.")
    except Exception as e:
        print(f"Error saat menghapus inventaris: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataInventaris()
def LihatDataInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data Inventaris"))
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM inventaris")
        inventaris = cursor.fetchall()
        if inventaris:
            print("Daftar Inventaris:")
            for item in inventaris:
                print(f"Nama: {item[1]}, Jumlah: {item[2]}")
        else:
            print("Tidak ada inventaris yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data inventaris: {e}")
    finally:
        cursor.close()
        conn.close()
    
    input("Tekan Enter untuk kembali...")
    ManagementDataInventaris()