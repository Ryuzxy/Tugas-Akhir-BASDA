import os
import pyfiglet
import tabulate
from db.DBKon import conn
def PanelAparat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format(f"Hallo ASN {username}"))
    print("Silahkan Pilih Menu:")
    print("1.Management Surat")
    print("2.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementSurat(username)
    elif pil == "2":
        conn.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Terima Kasih Telah Menggunakan System Kami"))  
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelAparat(username)

def ManagementSurat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat"))
    print("1.Tambah Surat")
    print("2.Hapus Surat")
    print("3.Tampilkan Surat")
    print("4.Tampilkan Surat Pengantar")
    print("5.Update Surat")
    print("6.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSurat(username)
    elif pil == "2":
        HapusSurat(username)
    elif pil == "3":
        LihatDataSurat(username)
    elif pil == "4":
        TampilkanSuratPengantar(username)
    elif pil == "5":
        UpdateSurat(username)
    elif pil == "6":
        PanelAparat(username)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSurat(username)
def TambahSurat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat"))
    print("Formulir untuk menambahkan surat akan ditampilkan di sini.")
    no_surat = input("Masukkan nomor surat: ")
    tanggal_surat = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    print("1. Pembuatan Surat Keterangan Domisili")
    print("2. Pembuatan SKCK")
    print("3. Surat Permohonan Bantuan Sosial")
    print("4. Pembuatan KK")
    print("5. Pembuatan Surat Keterangan Usaha")
    print("6. Pembuatan Surat Keterangan Tidak Mampu")
    print("7. Pembuatan Surat Keterangan Kematian")
    print("8. Pembuatan Surat Keterangan Lainnya")
    perihal = input("Masukkan perihal surat: ")
    print("1.Surat Keluar")
    print("2.Surat Masuk")
    print("3.Surat Sedang Diproses")
    keterangan = input("Masukkan keterangan surat: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO surat (nomor_surat, tanggal_surat, id_perihal, id_keterangan) VALUES (%s, %s, %s, %s)", (no_surat, tanggal_surat, perihal, keterangan))
        conn.commit()
        print("Surat berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan surat: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementSurat(username)
def HapusSurat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Surat"))
    DisplaySurat()
    no_surat = input("Masukkan nomor surat yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM surat WHERE no_surat = %s", (no_surat,))
        conn.commit()
        print("Surat berhasil dihapus.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus surat: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementSurat(username)
def LihatDataSurat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data Surat"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM surat")
        results = cursor.fetchall()
        if results:
            headers = ["Nomor Surat", "Tanggal Surat", "Perihal", "Keterangan"]
            print(tabulate.tabulate(results, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data surat yang tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data surat: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementSurat(username)
def TampilkanSuratPengantar(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Surat Pengantar"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM surat_pengantar")
        results = cursor.fetchall()
        if results:
            headers = ["Nomor Surat", "RW"]
            print(tabulate.tabulate(results, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data surat pengantar yang tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data surat pengantar: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementSurat(username)
def UpdateSurat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Update Surat"))
    DisplaySurat()
    no_surat = input("Masukkan nomor surat yang akan diupdate: ")
    tanggal_surat = input("Masukkan tanggal surat baru (YYYY-MM-DD): ")
    perihal = input("Masukkan perihal surat baru: ")
    keterangan = input("Masukkan keterangan surat baru: ")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE surat SET tanggal_surat = %s, id_perihal = %s, id_keterangan = %s WHERE nomor_surat = %s", (tanggal_surat, perihal, keterangan, no_surat))
        conn.commit()
        if cursor.rowcount > 0:
            print("Surat berhasil diupdate.")
        else:
            print("Nomor surat tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengupdate surat: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementSurat(username)
def DisplaySurat():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM surat")
        surat = cursor.fetchall()
        if surat:
            headers = ["No Surat", "Tanggal Surat", "Perihal", "Keterangan"]
            print(tabulate.tabulate(surat, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data surat yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data surat: {e}")
    finally:
        cursor.close()
