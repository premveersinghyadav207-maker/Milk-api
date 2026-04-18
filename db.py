import psycopg2

def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        database="milk_db",
        user="postgres",
        password="1234",
        port="5432"
    )
    return conn