import psycopg2

def Koneksi():
    return psycopg2.connect(
        dbname="Basda",
        user="postgres",
        password="Ryuxy27.",
        host="localhost",
        port="5432"
    )
def Koneksi2():
    conn = psycopg2.connect(
        dbname="Basda",
        user="postgres",
        password="Ryuxy27.",
        host="localhost",
        port="5432"
    )
    return conn

conn = psycopg2.connect(
    dbname="Basda",
    user="postgres",
    password="Ryuxy27.",
    host="localhost",
    port="5432"
)