import psycopg2

def Koneksi():
    return psycopg2.connect(
        dbname="Basda",
        user="postgres",
        password="Ryuxy27.",
        host="localhost",
        port="5432"
    )
