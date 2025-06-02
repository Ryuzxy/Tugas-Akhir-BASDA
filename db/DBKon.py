import psycopg2
conn = psycopg2.connect(
    dbname="Basda",
    user="postgres",
    password="120306",
    host="localhost",
    port="5432"
)