import datetime
import os
import tabulate
import pyfiglet
from db.DBKon import conn
def PanelRW(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format(f"Nihau, Pak {username}"))
    print("Silahkan Pilih Menu:")
    print("1.Tambah Surat Pengantar")
    print("2.Cek Data Bantuan Sosial")
    print("3.Keluar System")
    pil = input("Pilih Menu:" )
    if pil == "1":
        TambahSuratPengantar(username)
    elif pil == "2":
        CekDataBantuanSosial(username)
    elif pil == "3":
        print("Terima Kasih Telah Menggunakan System Kami")
        exit()
    else:   
        print("Pilihan tidak valid. Silakan coba lagi.")
        PanelRW(username)

def TambahSuratPengantar(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Tambah Surat Pengantar"))
    display_surat_pengantar()
    no_surat = input("Masukkan nomor surat pengantar: ")
    rw = input("Masukkan no RW: ")
    
    cursor = conn.cursor()
    try:
        # Cek apakah nomor surat sudah ada di tabel surat
        cursor.execute("SELECT * FROM surat WHERE nomor_surat = %s", (no_surat,))
        surat_exist = cursor.fetchone()

        # Jika belum ada, tambahkan surat terlebih dahulu
        if not surat_exist:
            tanggal_sekarang = datetime.date.today()
            keterangan = "4"
            print("1. Pembuatan Surat Keterangan Domisili")
            print("2. Pembuatan SKCK")
            print("3. Surat Permohonan Bantuan Sosial")
            print("4. Pembuatan KK")
            print("5. Pembuatan Surat Keterangan Usaha")
            print("6. Pembuatan Surat Keterangan Tidak Mampu")
            print("7. Pembuatan Surat Keterangan Kematian")
            print("8. Pembuatan Surat Keterangan Lainnya")
            perihal = input("Masukkan tujuan surat: ")
            cursor.execute(
                "INSERT INTO surat (nomor_surat, tanggal_surat, id_perihal, id_keterangan) VALUES (%s, %s, %s, %s)",
                (no_surat, tanggal_sekarang, perihal, keterangan)
            )
            print("Data surat berhasil ditambahkan ke tabel surat.")

        # Sekarang insert ke surat_pengantar
        cursor.execute(
            "INSERT INTO surat_pengantar (nomor_surat, id_rw) VALUES (%s, %s)",
            (no_surat, rw)
        )
        conn.commit()
        print("Surat pengantar berhasil ditambahkan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan surat pengantar: {e}")
        conn.rollback()
    finally:
        cursor.close()
        input("Tekan Enter untuk kembali ke menu utama...")
        PanelRW(username)


def CekDataBantuanSosial(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Cek Data Bantuan Sosial"))
    print("Data bantuan sosial akan ditampilkan di sini.")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM bantuan_sosial")
        results = cursor.fetchall()
        if results:
            headers = ["id_bantuan", "nama_bantuan"]
            print(tabulate.tabulate(results, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data bantuan sosial yang tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data bantuan sosial: {e}")
    finally:
        cursor.close()
    input("Tekan Enter untuk kembali ke menu utama...")
    PanelRW(username)

def display_surat_pengantar():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM surat_pengantar")
        results = cursor.fetchall()
        if results:
            headers = ["Nomor Surat", "ID RW"]
            print(tabulate.tabulate(results, headers=headers, tablefmt="double_grid"))
        else:
            print("Tidak ada data surat pengantar yang tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data surat pengantar: {e}")
    finally:
        cursor.close()