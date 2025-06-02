import os
import pyfiglet
from db.DBKon import conn
import tabulate
def PanelAdmin(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("SIMANDESA"))
    print(f"Selamat datang, {username}!")
    
    print("\nSilahkan Pilih Menu:")
    print("1.Management Data Login User")
    print("2.Management Data Inventaris Desa")
    print("3.Management Data Bantuan Sosial")
    print("4.Management Surat")
    print("5.Laporan Bulanan")
    print("6.Management Data Penduduk")
    print("7.Tampilkan Surat Pengantar")
    print("8.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        ManagementDataLoginUser(username)
    elif pil == "2":
        ManagementDataInventaris(username)
    elif pil == "3":
        ManagementDataBantuanSosial(username)
    elif pil == "4":
        ManagementSurat(username)
    elif pil == "5":
        LaporanBulanan(username)
    elif pil == "6":
        ManagementDataPenduduk(username)
    elif pil == "7":
        TampilkanSuratPengantar(username)
    elif pil == "8":
        conn.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Terima Kasih Telah Menggunakan System Kami"))  
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        print("Tekan Enter untuk kembali ke menu utama...")
        input()
        PanelAdmin()
def ManagementDataLoginUser(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Login User"))
    print("1.Tambah User")
    print("2.Hapus User")
    print("3.Lihat Data User")
    print("4.Update User")
    print("5.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahUser(username)
    elif pil == "2":
        HapusUser(username)
    elif pil == "3":
        LihatDataUser(username)
    elif pil == "4":
        UpdateUser(username)
    elif pil == "5":
        PanelAdmin(username)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataLoginUser(username)
def TambahUser(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah User"))
    DisplayUser()
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    role = input("Masukkan role (admin/asn/rw): ").lower()        
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
        input("Tekan Enter untuk kembali...")
        ManagementDataLoginUser(username)
def HapusUser(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus User"))
    DisplayUser()
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
    input("Tekan Enter untuk kembali...")
    ManagementDataLoginUser(username)
def LihatDataUser(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data User"))

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        if users:
            headers = ["id_user", "username", "password", "role"]
            print(tabulate.tabulate(users, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada user yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data user: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataLoginUser(username)

def UpdateUser(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Update User"))
    DisplayUser()
    username = input("Masukkan username yang akan diupdate: ")    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user:
            new_username = input(f"Masukkan username baru (tekan Enter untuk tetap {user[1]}): ") or user[1]
            new_password = input(f"Masukkan password baru (tekan Enter untuk tetap {user[2]}): ") or user[2]
            new_role = input(f"Masukkan role baru (tekan Enter untuk tetap {user[3]}): ") or user[3]
            
            cursor.execute("UPDATE users SET username = %s, password = %s, role = %s WHERE username = %s",
                        (new_username, new_password, new_role, username))
            conn.commit()
            print("User berhasil diupdate!")
        else:
            print("User tidak ditemukan.")
    except Exception as e:
        print(f"Error saat mengupdate user: {e}")
        conn.rollback()
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataLoginUser(username)
def DisplayUser():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        if users:
            headers = ["id_user", "username", "password", "role"]
            print(tabulate.tabulate(users, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada user yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data user: {e}")
    finally:
        cursor.close()
def ManagementDataInventaris(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Inventaris Desa"))
    print("1.Tambah Inventaris")
    print("2.Hapus Inventaris")
    print("3.Lihat Data Inventaris")
    print("4.Update Inventaris")
    print("5.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahInventaris(username)
    elif pil == "2":
        HapusInventaris(username)
    elif pil == "3":
        LihatDataInventaris(username)
    elif pil == "4":
        UpdateInventaris(username)
    elif pil == "5":
        PanelAdmin(username)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataInventaris(username)
def TambahInventaris(username):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Tambah Inventaris"))
        Display()
        nama_inventaris = input("Masukkan nama inventaris: ")
        jumlah = input("Masukkan jumlah inventaris: ")
        kondisi = input("Masukkan kondisi inventaris (1.sangat baik, 2.cukup baik, 3.perlu perbaikan): ")
        tanggal_masuk = input("Masukkan tanggal masuk inventaris (YYYY-MM-DD): ")
        
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO inventaris (nama_barang, jumlah_barang, id_kondisi, tanggal) VALUES (%s, %s, %s, %s)", (nama_inventaris, jumlah, kondisi, tanggal_masuk))
            conn.commit()
            print("Inventaris berhasil ditambahkan!")
        except Exception as e:
            print(f"Error saat menambahkan inventaris: {e}")
            conn.rollback()
        finally:
            cursor.close()
        input("Tekan Enter untuk kembali...")
        ManagementDataInventaris(username)
def HapusInventaris(username):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Hapus Inventaris"))
        Display()
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
        input("Tekan Enter untuk kembali...")
        ManagementDataInventaris(username)
def LihatDataInventaris(username):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Lihat Data Inventaris"))
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM inventaris")
            inventaris = cursor.fetchall()
            if inventaris:
                headers = ["ID", "Nama Inventaris", "Jumlah", "Kondisi", "Tanggal Masuk"]
                print(tabulate.tabulate(inventaris, headers=headers, tablefmt="double_grid"))
            else:
                print("Tidak ada inventaris yang terdaftar.")
        except Exception as e:
            print(f"Error saat mengambil data inventaris: {e}")
        finally:
            cursor.close()
        input("Tekan Enter untuk kembali...")
        ManagementDataInventaris(username)

def UpdateInventaris(username):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Update Inventaris"))
        Display()
        nama_inventaris = input("Masukkan nama inventaris yang akan diupdate: ")
        jumlah = input("Masukkan jumlah inventaris baru: ")
        kondisi = input("Masukkan kondisi inventaris baru (1.sangat baik, 2.cukup baik, 3.perlu perbaikan): ")
        tanggal_masuk = input("Masukkan tanggal masuk inventaris baru (YYYY-MM-DD): ")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE inventaris SET jumlah_barang = %s, id_kondisi = %s, tanggal = %s WHERE nama_barang = %s", (jumlah, kondisi, tanggal_masuk, nama_inventaris))
            conn.commit()
            if cursor.rowcount > 0:
                print("Inventaris berhasil diupdate!")
            else:
                print("Inventaris tidak ditemukan.")
        except Exception as e:
            print(f"Error saat mengupdate inventaris: {e}")
            conn.rollback()
        finally:
            cursor.close()
        input("Tekan Enter untuk kembali...")
        ManagementDataInventaris(username)
def Display():
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM inventaris")
            inventaris = cursor.fetchall()
            if inventaris:
                headers = ["ID", "Nama Inventaris", "Jumlah", "Kondisi", "Tanggal Masuk"]
                print(tabulate.tabulate(inventaris, headers=headers, tablefmt="double_grid"))
            else:
                print("Tidak ada inventaris yang terdaftar.")
        except Exception as e:
            print(f"Error saat mengambil data inventaris: {e}")
        finally:
            cursor.close()
def ManagementDataBantuanSosial(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Bantuan Sosial"))
    print("1.Tambah Data Bantuan Sosial")
    print("2.Hapus Data Bantuan Sosial")
    print("3.Lihat Data Bantuan Sosial")
    print("4.Update Data Bantuan Sosial")
    print("5.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataBantuanSosial(username)
    elif pil == "2":
        HapusDataBantuanSosial(username)
    elif pil == "3":
        LihatDataBantuanSosial(username)
    elif pil == "4":
        UpdateDataBantuanSosial(username)
    elif pil == "5":
        PanelAdmin(username)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataBantuanSosial(username)
def TambahDataBantuanSosial(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Bantuan Sosial"))
    DisplayBantuanSosial()
    id_bantuan = input("Masukkan ID Bantuan Sosial: ")
    nama = input("Masukkan nama: ")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO bantuan_sosial (id_bantuan, nama_bantuan) VALUES (%s, %s)", (id_bantuan, nama))
        conn.commit()
        print("Data Bantuan Sosial berhasil ditambahkan!")
    except Exception as e:
        print(f"Error saat menambahkan data bantuan sosial: {e}")
        conn.rollback()
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial(username)

def HapusDataBantuanSosial(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Data Bantuan Sosial"))
    DisplayBantuanSosial()
    id_bantuan = input("Masukkan ID Bantuan Sosial yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM bantuan_sosial WHERE id_bantuan = %s", (id_bantuan,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Data Bantuan Sosial berhasil dihapus!")
        else:
            print("Data Bantuan Sosial tidak ditemukan.")
    except Exception as e:
        print(f"Error saat menghapus data bantuan sosial: {e}")
        conn.rollback()
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial(username)
def LihatDataBantuanSosial(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data Bantuan Sosial"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM bantuan_sosial")
        bantuan_sosial = cursor.fetchall()
        if bantuan_sosial:
            headers = ["ID Bantuan", "Nama"]
            print(tabulate.tabulate(bantuan_sosial, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data bantuan sosial yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data bantuan sosial: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial(username)
def UpdateDataBantuanSosial(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Update Data Bantuan Sosial"))
    DisplayBantuanSosial()
    id_bantuan = input("Masukkan ID Bantuan Sosial yang akan diupdate: ")
    nama = input("Masukkan nama baru: ")
    
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE bantuan_sosial SET nama_bantuan = %s WHERE id_bantuan = %s", (nama, id_bantuan))
        conn.commit()
        if cursor.rowcount > 0:
            print("Data Bantuan Sosial berhasil diupdate!")
        else:
            print("Data Bantuan Sosial tidak ditemukan.")
    except Exception as e:
        print(f"Error saat mengupdate data bantuan sosial: {e}")
        conn.rollback()
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali...")
    ManagementDataBantuanSosial(username)
def DisplayBantuanSosial():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM bantuan_sosial")
        bantuan_sosial = cursor.fetchall()
        if bantuan_sosial:
            headers = ["ID Bantuan", "Nama"]
            print(tabulate.tabulate(bantuan_sosial, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data bantuan sosial yang terdaftar.")
    except Exception as e:
        print(f"Error saat mengambil data bantuan sosial: {e}")
    finally:
        cursor.close()
def ManagementSurat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Surat"))
    print("1.Tambah Surat")
    print("2.Hapus Surat")
    print("3.Lihat Data Surat")
    print("4.Update Surat")
    print("5.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSurat(username)
    elif pil == "2":
        HapusSurat(username)
    elif pil == "3":
        LihatDataSurat(username)
    elif pil == "4":
        UpdateSurat(username)
    elif pil == "5":
        PanelAdmin(username)
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
        cursor.execute("DELETE FROM surat WHERE nomor_surat = %s", (no_surat,))
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
    input("Tekan Enter untuk kembali...")
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
def LaporanBulanan(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Laporan Bulanan"))
    print("1.Lihat Laporan Bulanan")
    print("2.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        LihatLaporanBulanan(username)
    elif pil == "2":
        PanelAdmin(username)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        LaporanBulanan(username)
def LihatLaporanBulanan(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Laporan Bulanan - Admin: {username}\n")
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        tahun = int(input("Masukkan tahun (misal 2025): "))
        os.system('cls' if os.name == 'nt' else 'clear')
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk bulan dan tahun.")
        input("Tekan Enter untuk kembali...")
        return
    try:
        cursor = conn.cursor()
        print(f"📥 Surat Masuk - {bulan:02d}/{tahun}")
        cursor.execute("""
            SELECT nomor_surat, tanggal_surat, id_perihal
            FROM surat
            WHERE EXTRACT(MONTH FROM tanggal_surat) = %s AND EXTRACT(YEAR FROM tanggal_surat) = %s And id_keterangan = 2
        """, (bulan, tahun))
        data_masuk = cursor.fetchall()
        if data_masuk:
            print(tabulate.tabulate(data_masuk, headers=["Nomor Surat", "Tanggal", "Perihal"], tablefmt="double_grid"))
        else:
            print("Tidak ada data surat masuk untuk periode ini.")
        print("\n")
        print(f"📤 Surat Keluar - {bulan:02d}/{tahun}")
        cursor.execute("""
            SELECT nomor_surat, tanggal_surat, id_perihal
            FROM surat
            WHERE EXTRACT(MONTH FROM tanggal_surat) = %s AND EXTRACT(YEAR FROM tanggal_surat) = %s And id_keterangan = 1
        """, (bulan, tahun))
        data_keluar = cursor.fetchall()
        if data_keluar:
            print(tabulate.tabulate(data_keluar, headers=["Nomor Surat", "Tanggal", "Perihal"], tablefmt="double_grid"))
        else:
            print("Tidak ada data surat keluar untuk periode ini.")

        print("\n")
        print(f"📨 Surat Pengantar - {bulan:02d}/{tahun}")
        cursor.execute("""
            SELECT nomor_surat, tanggal_surat, id_perihal
            FROM surat
            WHERE EXTRACT(MONTH FROM tanggal_surat) = %s AND EXTRACT(YEAR FROM tanggal_surat) = %s and id_keterangan = 4
        """, (bulan, tahun))
        data_pengantar = cursor.fetchall()
        if data_pengantar:
            print(tabulate.tabulate(data_pengantar, headers=["Nomor Surat", "Tanggal", "Perihal"], tablefmt="double_grid"))
        else:
            print("Tidak ada data surat pengantar untuk periode ini.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil laporan: {e}")
    finally:
        cursor.close()
    input("\nTekan Enter untuk kembali ke menu...")
    LaporanBulanan(username)
def ManagementDataPenduduk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Management Data Penduduk"))
    print("1.Tambah Data Penduduk")
    print("2.Hapus Data Penduduk")
    print("3.Lihat Data Penduduk")
    print("4.Update Data Penduduk")
    print("5.Kembali ke Menu Utama")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahDataPenduduk(username)
    elif pil == "2":
        HapusDataPenduduk(username)
    elif pil == "3":
        LihatDataPenduduk(username)
    elif pil == "4":
        UpdateDataPenduduk(username)
    elif pil == "5":
        PanelAdmin(username)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        ManagementDataPenduduk(username)
def TambahDataPenduduk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Data Penduduk"))
    print("Formulir untuk menambahkan data penduduk akan ditampilkan di sini.")
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")
    tempat_lahir = input("Masukkan Tempat Lahir: ")
    tanggal_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (Laki-laki/Perempuan): ")
    rw = input("Masukkan No RW: ")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO penduduk (nik, nama_penduduk, tempat_lahir, tanggal_lahir, jenis_kelamin, id_rw)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nik, nama, tempat_lahir, tanggal_lahir, jenis_kelamin, rw))
        conn.commit()
        print("Data Penduduk berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan data penduduk: {e}")
    finally:
        cursor.close()
        input("Tekan Enter untuk kembali ke menu utama...")
        ManagementDataPenduduk(username)
def HapusDataPenduduk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Hapus Data Penduduk"))
    DisplayPenduduk()
    nik = input("Masukkan NIK penduduk yang akan dihapus: ")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM penduduk WHERE nik = %s", (nik,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Data Penduduk berhasil dihapus.")
        else:
            print("Data Penduduk tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus data penduduk: {e}")
    finally:
        cursor.close()
        input("Tekan Enter untuk kembali ke menu utama...")
        ManagementDataPenduduk(username)
def LihatDataPenduduk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Lihat Data Penduduk"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM penduduk")
        penduduk = cursor.fetchall()
        if penduduk:
            headers = ["NIK", "Nama",  "Tanggal Lahir", "Jenis Kelamin", "RW", "Tempat Lahir"]
            print(tabulate.tabulate(penduduk, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data penduduk yang terdaftar.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data penduduk: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementDataPenduduk(username)
def UpdateDataPenduduk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Update Data Penduduk"))
    DisplayPenduduk()
    nik = input("Masukkan NIK penduduk yang akan diupdate: ")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM penduduk WHERE nik = %s", (nik,))
        penduduk = cursor.fetchone()
        if penduduk:
            nama = input(f"Masukkan Nama baru (tekan Enter untuk tetap {penduduk[1]}): ") or penduduk[1]
            tempat_lahir = input(f"Masukkan Tempat Lahir baru (tekan Enter untuk tetap {penduduk[2]}): ") or penduduk[2]
            tanggal_lahir = input(f"Masukkan Tanggal Lahir baru (YYYY-MM-DD, tekan Enter untuk tetap {penduduk[3]}): ") or penduduk[3]
            jenis_kelamin = input(f"Masukkan Jenis Kelamin baru (L/P, tekan Enter untuk tetap {penduduk[4]}): ").upper() or penduduk[4]
            rw = input(f"Masukkan No RW baru (tekan Enter untuk tetap {penduduk[5]}): ") or penduduk[5]
            
            cursor.execute("""
                UPDATE penduduk
                SET nama = %s, tempat_lahir = %s, tanggal_lahir = %s, jenis_kelamin = %s, rw = %s
                WHERE nik = %s
            """, (nama, tempat_lahir, tanggal_lahir, jenis_kelamin, rw, nik))
            conn.commit()
            print("Data Penduduk berhasil diupdate.")
        else:
            print("Data Penduduk tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengupdate data penduduk: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    ManagementDataPenduduk(username)
def DisplayPenduduk():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM penduduk")
        penduduk = cursor.fetchall()
        if penduduk:
            headers = ["NIK", "Nama", "Tanggal Lahir",  "Jenis Kelamin", "RW","Tempat Lahir"]
            print(tabulate.tabulate(penduduk, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data penduduk yang terdaftar.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data penduduk: {e}")
    finally:
        cursor.close()
def TampilkanSuratPengantar(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tampilkan Surat Pengantar"))
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM surat_pengantar")
        results = cursor.fetchall()
        if results:
            headers = ["nomor_surat", "rw"]
            print(tabulate.tabulate(results, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data surat pengantar yang tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data surat pengantar: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    PanelAdmin(username)