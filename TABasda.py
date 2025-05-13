import psycopg2
import pyfiglet
import os
import pandas as pd

# Koneksi ke database
conn = psycopg2.connect(
    dbname="TABasda",
    user="postgres",
    password="Ryuxy27.",
    host="localhost",
    port="5432"
)
def koneksi_awal():
    conn = psycopg2.connect(
        dbname="TABasda",
        user="postgres",
        password="Ryuxy27.",
        host="localhost",
        port="5432"
    )
    return conn
        

def LoginAdmin():
    koneksi_awal()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Login Admin"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'Admin'", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login berhasil!")
        PanelAdmin()
    else: 
        print("Login gagal! Anda Bukan Admin Dari System.")
        cursor.close()
        conn.close()
        input("Tekan Enter untuk mencoba ulang...")
        LoginAdmin()

def LoginAparat():
    koneksi_awal()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Login Aparat"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = 'ASN'", (username, password))
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

def LoginKades():
    koneksi_awal()
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

def PanelAdmin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang Admin"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Data Login User")
    print("2.Hapus/Ubah Data Login User")
    print("3.Tampilkan Data Login User")
    print("4.Tambah Data Inventaris Desa")
    print("5.Hapus/Ubah Data Inventaris Desa")
    print("6.Tampilkan Data Inventaris Desa")
    print("7.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataLoginUser()
    elif pil == "2":
        HapusOrUbahDataLoginUser()
    elif pil == "3":
        TampilkanDataLoginUser()
    elif pil == "4":
        TambahDataInventaris()
    elif pil == "5":
        HapusOrUbahDataInventaris()
    elif pil == "6":
        TampilkanDataInventaris()
    elif pil == "7":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelAdmin()
    

def PanelAparat():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang ASDA"))
    print("Silahkan Pilih Menu:")
    print("1.Managemet Surat Masuk")
    print("2.Managemet Surat Keluar")
    print("3.Management Data Penduduk")
    print("4.Management Data Bantuan Sosial")
    print("5.Laporan Bulanan ")
    print("6.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementSuratMasuk()
    elif pil == "2":
        ManagementSuratKeluar()
    elif pil == "3":
        ManagementDataPenduduk()
    elif pil == "4":
        ManagementDataBantuanSosial()
    elif pil == "5":
        LaporanBulanan()
    elif pil == "6":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelAparat()

def PanelKades():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang Kades"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Surat Pengantar")
    print("2.Cek Status Surat Pengantar")
    print("3.Cek Data Bantuan Sosial")
    print("4.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratPengantar()
    elif pil == "2":
        CekStatusSuratPengantar()
    elif pil == "3":
        CekDataBantuanSosial()
    elif pil == "4":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:   
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelKades()
    
def TambahDataLoginUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Login User"))
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    role = input("Masukkan role (admin/aparat/kades): ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    conn.commit()
    cursor.close()
    
    print("Data login user berhasil ditambahkan!")
    PanelAdmin()

def HapusOrUbahDataLoginUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus/Ubah Data Login User"))
    username = input("Masukkan username yang ingin dihapus/ubah: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Username: {result[0]}")
        print(f"Password: {result[1]}")
        print(f"Role: {result[2]}")
        
        pilihan = input("Apakah Anda ingin menghapus (h) atau mengubah (u) data ini? (h/u): ")
        if pilihan.lower() == 'h':
            cursor.execute("DELETE FROM users WHERE username = %s", (username,))
            conn.commit()
            print("Data berhasil dihapus!")
        elif pilihan.lower() == 'u':
            new_password = input("Masukkan password baru: ")
            new_role = input("Masukkan role baru (admin/aparat/kades): ")
            cursor.execute("UPDATE users SET password = %s, role = %s WHERE username = %s", (new_password, new_role, username))
            conn.commit()
            print("Data berhasil diubah!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    HapusOrUbahDataLoginUser()

def TampilkanDataLoginUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Data Login User"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    
    if result:
        print("Data Login User:")
        for row in result:
            print(f"Username: {row[0]}, Password: {row[1]}, Role: {row[2]}")
    else:
        print("Tidak ada data login user.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu admin...")
    PanelAdmin()

def TambahDataInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Inventaris"))
    cursor = conn.cursor()
    nama_barang = input("Masukkan nama barang: ")
    jumlah_barang = input("Masukkan jumlah barang: ")
    tanggal = input("Masukkan tanggal barang ditambahkan (YYYY-MM-DD): ")
    kondisi_barang = input("Masukkan kondisi barang (baik/rusak): ")
    cursor.execute("INSERT INTO inventaris (nama_barang, jumlah_barang, tanggal, kondisi_barang) VALUES (%s, %s, %s, %s)", (nama_barang, jumlah_barang, tanggal, kondisi_barang))
    conn.commit()
    cursor.close()
    print("Data inventaris berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu admin...")
    PanelAdmin()

def HapusOrUbahDataInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus/Ubah Data Inventaris"))
    nama_barang = input("Masukkan nama barang yang ingin dihapus/ubah: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventaris WHERE nama_barang = %s", (nama_barang,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nama Barang: {result[0]}")
        print(f"Jumlah Barang: {result[1]}")
        print(f"Tanggal: {result[2]}")
        print(f"Kondisi Barang: {result[3]}")
        
        pilihan = input("Apakah Anda ingin menghapus (h) atau mengubah (u) data ini? (h/u): ")
        if pilihan.lower() == 'h':
            cursor.execute("DELETE FROM inventaris WHERE nama_barang = %s", (nama_barang,))
            conn.commit()
            print("Data berhasil dihapus!")
        elif pilihan.lower() == 'u':
            new_jumlah_barang = input("Masukkan jumlah barang baru: ")
            new_tanggal = input("Masukkan tanggal barang ditambahkan baru (YYYY-MM-DD): ")
            new_kondisi_barang = input("Masukkan kondisi barang baru (baik/rusak): ")
            cursor.execute("UPDATE inventaris SET jumlah_barang = %s, tanggal = %s, kondisi_barang = %s WHERE nama_barang = %s", (new_jumlah_barang, new_tanggal, new_kondisi_barang, nama_barang))
            conn.commit()
            print("Data berhasil diubah!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    HapusOrUbahDataInventaris()

def TampilkanDataInventaris():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Data Inventaris"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventaris")
    result = cursor.fetchall()
    if result:
        print("Data Inventaris:")
        for row in result:
            print(f"Nama Barang: {row[0]}, Jumlah Barang: {row[1]}, Tanggal: {row[2]}, Kondisi Barang: {row[3]}")
    else:
        print("Tidak ada data inventaris.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu admin...")
    PanelAdmin()

def ManagementSuratMasuk():
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("Management Surat Masuk"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Surat Masuk")
    print("2.Hapus/Ubah Surat Masuk")
    print("3.Tampilkan Surat Masuk")
    print("4.Tampilkan Surat Pengantar")
    print("5.Approve Surat Pengantar")
    print("6.Kembali Ke Menu ASBA")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratMasuk()
    elif pil == "2":
        HapusOrUbahSuratMasuk()
    elif pil == "3":
        TampilkanSuratMasuk()
    elif pil == "4":
        TampilkanSuratPengantar()
    elif pil == "5":
        ApproveSuratPengantar()
    elif pil == "6":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementSuratMasuk()
        
def TambahSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Masuk"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    pengirim = input("Masukkan nama pengirim: ")
    perihal = input("Masukkan perihal surat: ")       
    cursor = conn.cursor()
    cursor.execute("INSERT INTO surat_masuk (nomor_surat, tanggal, pengirim, perihal) VALUES (%s, %s, %s, %s)", (nomor_surat, tanggal, pengirim, perihal))
    conn.commit()
    cursor.close()       
    print("Surat berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratMasuk()
def HapusOrUbahSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus/Ubah Surat Masuk"))
    nomor_surat = input("Masukkan nomor surat yang ingin dihapus/ubah: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_masuk WHERE nomor_surat = %s", (nomor_surat,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nomor Surat: {result[0]}")
        print(f"Tanggal: {result[1]}")
        print(f"Pengirim: {result[2]}")
        print(f"Perihal: {result[3]}")
        pilihan = input("Apakah Anda ingin menghapus (h) atau mengubah (u) data ini? (h/u): ")
        if pilihan.lower() == 'h':
            cursor.execute("DELETE FROM surat_masuk WHERE nomor_surat = %s", (nomor_surat,))
            conn.commit()
            print("Data berhasil dihapus!")
        elif pilihan.lower() == 'u':
            new_tanggal = input("Masukkan tanggal surat baru (YYYY-MM-DD): ")
            new_pengirim = input("Masukkan nama pengirim baru: ")
            new_perihal = input("Masukkan perihal surat baru: ")
            cursor.execute("UPDATE surat_masuk SET tanggal = %s, pengirim = %s, perihal = %s WHERE nomor_surat = %s", (new_tanggal, new_pengirim, new_perihal, nomor_surat))
            conn.commit()
            print("Data berhasil diubah!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratMasuk()

def TampilkanSuratMasuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Surat Masuk"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_masuk")
    result = cursor.fetchall()
    if result:
        print("Data Surat Masuk:")
        for row in result:
            print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}")
    else:
        print("Tidak ada data surat masuk.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratMasuk()

def TampilkanSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Surat Pengantar"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_pengantar")
    result = cursor.fetchall()
    if result:
        print("Data Surat Pengantar:")
        for row in result:
            print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}")
    else:
        print("Tidak ada data surat pengantar.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratMasuk()

def ApproveSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Approve Surat Pengantar"))
    TampilkanSuratPengantar()
    print("Silahkan Masukkan Nomor Surat Pengantar yang ingin di approve:")
    nomor_surat = input("Masukkan nomor surat: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_pengantar WHERE nomor_surat = %s", (nomor_surat,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nomor Surat: {result[0]}")
        print(f"Tanggal: {result[1]}")
        print(f"Pengirim: {result[2]}")
        print(f"Perihal: {result[3]}")
        
        pilihan = input("Apakah Anda ingin menyetujui (y) atau menolak (n) surat ini? (y/n): ")
        if pilihan.lower() == 'y':
            cursor.execute("UPDATE surat_pengantar SET status = 'disetujui' WHERE nomor_surat = %s", (nomor_surat,))
            conn.commit()
            print("Surat berhasil disetujui!")
        elif pilihan.lower() == 'n':
            cursor.execute("UPDATE surat_pengantar SET status = 'ditolak' WHERE nomor_surat = %s", (nomor_surat,))
            conn.commit()
            print("Surat berhasil ditolak!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratMasuk()

def ManagementSuratKeluar():    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat Keluar"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Surat Keluar")
    print("2.Hapus/Ubah Surat Keluar")
    print("3.Tampilkan Surat Keluar")
    print("4.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratKeluar()
    elif pil == "2":
        HapusOrUbahSuratKeluar()
    elif pil == "3":
        TampilkanSuratKeluar()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk kembali ke menu ASBA...")
        ManagementSuratKeluar()

def TambahSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Keluar"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    penerima = input("Masukkan nama penerima: ")
    perihal = input("Masukkan perihal surat: ")       
    cursor = conn.cursor()
    cursor.execute("INSERT INTO surat_keluar (nomor_surat, tanggal, penerima, perihal) VALUES (%s, %s, %s, %s)", (nomor_surat, tanggal, penerima, perihal))
    conn.commit()
    cursor.close()       
    print("Surat berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratKeluar()

def HapusOrUbahSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus/Ubah Surat Keluar"))
    TampilkanSuratKeluar()
    print("Silahkan Masukkan Nomor Surat Keluar yang ingin dihapus/ubah:")
    nomor_surat = input("Masukkan nomor surat: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_keluar WHERE nomor_surat = %s", (nomor_surat,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nomor Surat: {result[0]}")
        print(f"Tanggal: {result[1]}")
        print(f"Penerima: {result[2]}")
        print(f"Perihal: {result[3]}")
        
        pilihan = input("Apakah Anda ingin menghapus (h) atau mengubah (u) data ini? (h/u): ")
        if pilihan.lower() == 'h':
            cursor.execute("DELETE FROM surat_keluar WHERE nomor_surat = %s", (nomor_surat,))
            conn.commit()
            print("Data berhasil dihapus!")
        elif pilihan.lower() == 'u':
            new_tanggal = input("Masukkan tanggal surat baru (YYYY-MM-DD): ")
            new_penerima = input("Masukkan nama penerima baru: ")
            new_perihal = input("Masukkan perihal surat baru: ")
            cursor.execute("UPDATE surat_keluar SET tanggal = %s, penerima = %s, perihal = %s WHERE nomor_surat = %s", (new_tanggal, new_penerima, new_perihal, nomor_surat))
            conn.commit()
            print("Data berhasil diubah!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratKeluar()

def TampilkanSuratKeluar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Surat Keluar"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_keluar")
    result = cursor.fetchall()
    if result:
        print("Data Surat Keluar:")
        for row in result:
            print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Penerima: {row[2]}, Perihal: {row[3]}")
    else:
        print("Tidak ada data surat keluar.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementSuratKeluar()

def ManagementDataPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Penduduk"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Data Penduduk")
    print("2.Hapus/Ubah Data Penduduk")
    print("3.Tampilkan Data Penduduk")
    print("4.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataPenduduk()
    elif pil == "2":
        HapusOrUbahDataPenduduk()
    elif pil == "3":
        TampilkanDataPenduduk()
    elif pil == "4":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk kembali ke menu ASBA...")
        ManagementDataPenduduk()

def TambahDataPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Penduduk"))
    nama = input("Masukkan nama penduduk: ")
    nik = input("Masukkan NIK: ")
    alamat = input("Masukkan alamat: ")
    jenis_kelamin = input("Masukkan jenis kelamin: ")
    tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO penduduk (nama, nik, alamat, tanggal_lahir,jenis_kelamin) VALUES (%s, %s, %s, %s, %s)", (nama, nik, alamat, tanggal_lahir, jenis_kelamin))
    conn.commit()
    cursor.close()       
    print("Data penduduk berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataPenduduk()

def HapusOrUbahDataPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus/Ubah Data Penduduk"))
    TampilkanDataPenduduk()
    nik = input("Masukkan NIK: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM penduduk WHERE nik = %s", (nik,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nama: {result[0]}")
        print(f"NIK: {result[1]}")
        print(f"Alamat: {result[2]}")
        print(f"Tanggal Lahir: {result[3]}")
        
        pilihan = input("Apakah Anda ingin menghapus (h) atau mengubah (u) data ini? (h/u): ")
        if pilihan.lower() == 'h':
            cursor.execute("DELETE FROM penduduk WHERE nik = %s", (nik,))
            conn.commit()
            print("Data berhasil dihapus!")
        elif pilihan.lower() == 'u':
            new_nama = input("Masukkan nama baru: ")
            new_alamat = input("Masukkan alamat baru: ")
            new_tanggal_lahir = input("Masukkan tanggal lahir baru (YYYY-MM-DD): ")
            cursor.execute("UPDATE penduduk SET nama = %s, alamat = %s, tanggal_lahir = %s WHERE nik = %s", (new_nama, new_alamat, new_tanggal_lahir, nik))
            conn.commit()
            print("Data berhasil diubah!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataPenduduk()

def TampilkanDataPenduduk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Data Penduduk"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM penduduk")
    result = cursor.fetchall()
    if result:
        print("Data Penduduk:")
        for row in result:
            print(f"Nama: {row[0]}, NIK: {row[1]}, Alamat: {row[2]}, Tanggal Lahir: {row[3]}")
    else:
        print("Tidak ada data penduduk.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataPenduduk()

def ManagementDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Bantuan Sosial"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Data Bantuan Sosial")
    print("2.Hapus/Ubah Data Bantuan Sosial")
    print("3.Tampilkan Data Bantuan Sosial")
    print("4.Ubah Status Bantuan Sosial")
    print("5.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataBantuanSosial()
    elif pil == "2":
        HapusOrUbahDataBantuanSosial()
    elif pil == "3":
        TampilkanDataBantuanSosial()
    elif pil == "4":
        UbahStatusBantuanSosial()
    elif pil == "5":
        PanelAparat()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk kembali ke menu ASBA...")
        ManagementDataBantuanSosial()

def TambahDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Bantuan Sosial"))
    nama = input("Masukkan nama penerima: ")
    nik = input("Masukkan NIK: ")
    jenis_bantuan = input("Masukkan jenis bantuan: ")
    tanggal = input("Masukkan tanggal bantuan diberikan (YYYY-MM-DD): ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bantuan_sosial (nama, nik, jenis_bantuan, tanggal) VALUES (%s, %s, %s, %s)", (nama, nik, jenis_bantuan, tanggal))
    conn.commit()
    cursor.close()       
    print("Data bantuan sosial berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataBantuanSosial()

def HapusOrUbahDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus/Ubah Data Bantuan Sosial"))
    TampilkanDataBantuanSosial()
    nik = input("Masukkan NIK: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bantuan_sosial WHERE nik = %s", (nik,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nama: {result[0]}")
        print(f"NIK: {result[1]}")
        print(f"Jenis Bantuan: {result[2]}")
        print(f"Tanggal: {result[3]}")
        
        pilihan = input("Apakah Anda ingin menghapus (h) atau mengubah (u) data ini? (h/u): ")
        if pilihan.lower() == 'h':
            cursor.execute("DELETE FROM bantuan_sosial WHERE nik = %s", (nik,))
            conn.commit()
            print("Data berhasil dihapus!")
        elif pilihan.lower() == 'u':
            new_nama = input("Masukkan nama baru: ")
            new_jenis_bantuan = input("Masukkan jenis bantuan baru: ")
            new_tanggal = input("Masukkan tanggal bantuan baru (YYYY-MM-DD): ")
            cursor.execute("UPDATE bantuan_sosial SET nama = %s, jenis_bantuan = %s, tanggal = %s WHERE nik = %s", (new_nama, new_jenis_bantuan, new_tanggal, nik))
            conn.commit()
            print("Data berhasil diubah!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataBantuanSosial()

def TampilkanDataBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Data Bantuan Sosial"))
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
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataBantuanSosial()

def UbahStatusBantuanSosial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Ubah Status Bantuan Sosial"))
    nik = input("Masukkan NIK: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bantuan_sosial WHERE nik = %s", (nik,))
    result = cursor.fetchone()
    if result:
        print("Data ditemukan:")
        print(f"Nama: {result[0]}")
        print(f"NIK: {result[1]}")
        print(f"Jenis Bantuan: {result[2]}")
        print(f"Tanggal: {result[3]}")
        
        pilihan = input("Apakah Anda ingin mengubah status bantuan sosial ini? (y/n): ")
        if pilihan.lower() == 'y':
            new_status = input("Masukkan status baru (disetujui/ditolak): ")
            cursor.execute("UPDATE bantuan_sosial SET status = %s WHERE nik = %s", (new_status, nik))
            conn.commit()
            print("Status berhasil diubah!")
        else:
            print("Tidak ada perubahan.")
    else:
        print("Data tidak ditemukan.")
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASBA...")
    ManagementDataBantuanSosial()

def LaporanBulanan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Laporan Bulanan"))
    cursor = conn.cursor()
    cursor.execute("SELECT * COUNT(*) FROM surat_masuk WHERE EXTRACT(MONTH FROM tanggal) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM tanggal) = EXTRACT(YEAR FROM CURRENT_DATE)")
    cursor.execute("SELECT * COUNT(*) FROM surat_keluar WHERE EXTRACT(MONTH FROM tanggal) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM tanggal) = EXTRACT(YEAR FROM CURRENT_DATE)")
    cursor.execute("SELECT * COUNT(*) FROM bantuan_sosial WHERE EXTRACT(MONTH FROM tanggal) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM tanggal) = EXTRACT(YEAR FROM CURRENT_DATE)")
    cursor.execute("SELECT * COUNT(*) FROM surat_pengantar WHERE EXTRACT(MONTH FROM tanggal) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM tanggal) = EXTRACT(YEAR FROM CURRENT_DATE)")
    result = cursor.fetchall()
    if result:
        print("Laporan Bulanan:")
        print(f"Jumlah Surat Masuk: {result[0][0]}")
        print(f"Jumlah Surat Keluar: {result[1][0]}")
        print(f"Jumlah Bantuan Sosial: {result[2][0]}")
        print(f"Jumlah Surat Pengantar: {result[3][0]}")
    else:
        print("Tidak ada data laporan bulanan.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu ASDA...")
    PanelKades()

def TambahSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Pengantar"))
    nomor_surat = input("Masukkan nomor surat: ")
    tanggal = input("Masukkan tanggal surat (YYYY-MM-DD): ")
    pengirim = input("Masukkan nama pengirim: ")
    perihal = input("Masukkan perihal surat: ")       
    cursor = conn.cursor()
    cursor.execute("INSERT INTO surat_pengantar (nomor_surat, tanggal, pengirim, perihal) VALUES (%s, %s, %s, %s)", (nomor_surat, tanggal, pengirim, perihal))
    conn.commit()
    cursor.close()       
    print("Surat pengantar berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu KADES...")
    PanelKades()

def CekStatusSuratPengantar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Cek Status Surat Pengantar"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM surat_pengantar")
    result = cursor.fetchall()
    if result:
        print("Data Surat Pengantar:")
        for row in result:
            print(f"Nomor Surat: {row[0]}, Tanggal: {row[1]}, Pengirim: {row[2]}, Perihal: {row[3]}, Status: {row[4]}")
    else:
        print("Tidak ada data surat pengantar.")
    
    cursor.close()
    input("Tekan Enter untuk kembali ke menu KADES...")
    PanelKades()

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

def MainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang di SIMANDESA"))
    print("Silahkan Login Sebagai:")
    print("1.Admin")
    print("2.Aparat")
    print("3.Kades")
    print("4.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        LoginAdmin()
    elif pil == "2":
        LoginAparat()
    elif pil == "3":
        LoginKades()
    elif pil == "4":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        MainMenu()

#Perintah
MainMenu()