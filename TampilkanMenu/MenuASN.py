import os
import pyfiglet
from db.DBKon import Koneksi as conn
def PanelAparat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format(f"Hallo ASN {username}"))
    print("Silahkan Pilih Menu:")
    print("1.Management Surat")
    print("2.Management Data Penduduk")
    print("3.Management Data Bantuan Sosial")
    print("4.Laporan Bulanan")
    print("5.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementSurat()
    elif pil == "2":
        ManagementDataPenduduk()
    elif pil == "3":
        ManagementDataBantuanSosial()
    elif pil == "4":
        LaporanBulanan()
    elif pil == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Terima Kasih Telah Menggunakan System Kami"))  
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelAparat(username)
        
def ManagementSurat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat"))
    print("1.Management Surat Masuk")
    print("2.Management Surat Keluar")
    print("3.Management Surat Pengantar")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementSuratMasuk()
    elif pil == "2":
        ManagementSuratKeluar()
    elif pil == "3":
        ManagementSuratPengantar()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSurat()

def ManagementDataPenduduk():  
    os.system('cls' if os.name == 'nt' else ' clear')
    print(pyfiglet.figlet_format("Management Data Penduduk"))
    print("1.Tambah Penduduk")
    print("2.Hapus Penduduk")
    print("3.Lihat Data Penduduk")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahPenduduk()
    elif pil == "2":
        HapusPenduduk()
    elif pil == "3":
        LihatDataPenduduk()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataPenduduk()
    
def ManagementDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Bantuan Sosial"))
    print("1.Tambah Data Bantuan Sosial")
    print("2.Hapus Data Bantuan Sosial")
    print("3.Lihat Data Bantuan Sosial")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataBantuanSosial()
    elif pil == "2":
        HapusDataBantuanSosial()
    elif pil == "3":
        LihatDataBantuanSosial()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataBantuanSosial()
    
def ManagementSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat Masuk"))
    print("1.Tambah Surat Masuk")
    print("2.Hapus Surat Masuk")
    print("3.Lihat Surat Masuk")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratMasuk()
    elif pil == "2":
        HapusSuratMasuk()
    elif pil == "3":
        LihatSuratMasuk()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSuratMasuk()

def ManagementSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat Keluar"))
    print("1.Tambah Surat Keluar")
    print("2.Hapus Surat Keluar")
    print("3.Lihat Surat Keluar")
    print("4.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratKeluar()
    elif pil == "2":
        HapusSuratKeluar()
    elif pil == "3":
        LihatSuratKeluar()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSuratKeluar()

def ManagementSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat Pengantar"))
    print("1.Acc Surat Pengantar")
    print("2.Tampilkan Surat Pengantar")
    print("3.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        AccSuratPengantar()
    elif pil == "2":
        TampilkanSuratPengantar()
    elif pil == "3":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSuratPengantar()

def LaporanBulanan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Laporan Bulanan"))
    print("1.Lihat Laporan Bulanan")
    print("2.Cetak Laporan Bulanan")
    print("3.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        LihatLaporanBulanan()
    elif pil == "2":
        CetakLaporanBulanan()
    elif pil == "3":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        LaporanBulanan()
    
def TambahPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Penduduk"))
    nama = input("Masukkan nama penduduk: ")
    nik = input("Masukkan NIK penduduk: ")
    alamat = input("Masukkan alamat penduduk: ")
    jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
    tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
    rt = input("Masukkan RT: ")
    rw = input("Masukkan RW: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Penduduk (nama, nik, alamat, jenis_kelamin, tanggal_lahir, rt, rw) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (nama, nik, alamat, jenis_kelamin, tanggal_lahir, rt, rw))
        conn.commit()
        print("Data penduduk berhasil ditambahkan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataPenduduk()

def HapusPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Penduduk"))
    nik = input("Masukkan NIK penduduk yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Penduduk WHERE nik = ?", (nik,))
        conn.commit()
        print("Data penduduk berhasil dihapus.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataPenduduk()
    
def LihatDataPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data Penduduk"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Penduduk")
        rows = cursor.fetchall()
        if rows:
            print("Data Penduduk:")
            for row in rows:
                print(f"NIK: {row[1]}, Nama: {row[0]}, Alamat: {row[2]}, Jenis Kelamin: {row[3]}, Tanggal Lahir: {row[4]}, RT: {row[5]}, RW: {row[6]}")
        else:
            print("Tidak ada data penduduk.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataPenduduk()

def TambahDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Bantuan Sosial"))
    tanggal = input("Masukkan tanggal bantuan (YYYY-MM-DD): ")
    nama_penduduk = input("Masukkan nama penerima bantuan: ")
    status = input("Masukkan status bantuan (Aktif/Tidak Aktif): ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO bantuan_sosial (tanggal, nama_penduduk, status) VALUES (?, ?, ?)",
                       (tanggal, nama_penduduk, status))
        conn.commit()
        print("Data bantuan sosial berhasil ditambahkan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial()

def HapusDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Data Bantuan Sosial"))
    nama_penduduk = input("Masukkan nama penerima bantuan yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM bantuan_sosial WHERE nama_penduduk = ?", (nama_penduduk,))
        conn.commit()
        print("Data bantuan sosial berhasil dihapus.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial()

def LihatDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data Bantuan Sosial"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM bantuan_sosial")
        rows = cursor.fetchall()
        if rows:
            print("Data Bantuan Sosial:")
            for row in rows:
                print(f"Tanggal: {row[0]}, Nama Penerima: {row[1]}, Status: {row[2]}")
        else:
            print("Tidak ada data bantuan sosial.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial()

def TambahSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Masuk"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    pengirim = input("Masukkan nama pengirim: ")
    perihal = input("Masukkan perihal surat: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Surat_masuk (nomor_surat, tanggal, pengirim, perihal) VALUES (?, ?, ?, ?)",
                       (nomor_surat, tanggal, pengirim, perihal))
        conn.commit()
        print("Data surat masuk berhasil ditambahkan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratMasuk()

def HapusSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Surat Masuk"))
    nomor_surat = input("Masukkan nomor surat yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Surat_masuk WHERE nomor_surat = ?", (nomor_surat,))
        conn.commit()
        print("Data surat masuk berhasil dihapus.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratMasuk()
def LihatSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Surat Masuk"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Surat_masuk")
        rows = cursor.fetchall()
        if rows:
            print("Data Surat Masuk:")
            for row in rows:
                print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}")
        else:
            print("Tidak ada data surat masuk.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratMasuk()
def TambahSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Keluar"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    penerima = input("Masukkan nama penerima: ")
    perihal = input("Masukkan perihal surat: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Surat_keluar (nomor_surat, tanggal, penerima, perihal) VALUES (?, ?, ?, ?)",
                       (nomor_surat, tanggal, penerima, perihal))
        conn.commit()
        print("Data surat keluar berhasil ditambahkan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratKeluar()
def HapusSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Surat Keluar"))
    nomor_surat = input("Masukkan nomor surat yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Surat_keluar WHERE nomor_surat = ?", (nomor_surat,))
        conn.commit()
        print("Data surat keluar berhasil dihapus.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratKeluar()
def LihatSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Surat Keluar"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Surat_keluar")
        rows = cursor.fetchall()
        if rows:
            print("Data Surat Keluar:")
            for row in rows:
                print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Penerima: {row[2]}, Perihal: {row[3]}")
        else:
            print("Tidak ada data surat keluar.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratKeluar() 
def AccSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Acc Surat Pengantar"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Surat_pengantar WHERE status = 'pending'")
        rows = cursor.fetchall()
        if rows:
            print("Data Surat Pengantar yang perlu di-ACC:")
            for row in rows:
                print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}")
        else:
            print("Tidak ada data surat pengantar yang perlu di-ACC.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratPengantar()

def TampilkanSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Surat Pengantar"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Surat_pengantar")
        rows = cursor.fetchall()
        if rows:
            print("Data Surat Pengantar:")
            for row in rows:
                print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}, Status: {row[4]}")
        else:
            print("Tidak ada data surat pengantar.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    ManagementSuratPengantar()

def LihatLaporanBulanan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Laporan Bulanan"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM laporan_bulanan")
        rows = cursor.fetchall()
        if rows:
            print("Data Laporan Bulanan:")
            for row in rows:
                print(f"Bulan: {row[0]}, Jumlah Surat Masuk: {row[1]}, Jumlah Surat Keluar: {row[2]}")
        else:
            print("Tidak ada data laporan bulanan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    LaporanBulanan()
def CetakLaporanBulanan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Cetak Laporan Bulanan"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM laporan_bulanan")
        rows = cursor.fetchall()
        if rows:
            with open("laporan_bulanan.txt", "w") as file:
                for row in rows:
                    file.write(f"Bulan: {row[0]}, Jumlah Surat Masuk: {row[1]}, Jumlah Surat Keluar: {row[2]}\n")
            print("Laporan bulanan berhasil dicetak ke laporan_bulanan.txt")
        else:
            print("Tidak ada data laporan bulanan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    finally:
        cursor.close()
        conn.close()
    input("Tekan Enter untuk kembali...")
    LaporanBulanan()

