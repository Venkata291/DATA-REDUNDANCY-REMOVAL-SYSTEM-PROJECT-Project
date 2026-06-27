import psycopg2

def get_connection():
    return psycopg2.connect(
        database="redundancydb",
        user="admin",
        password="admin123",
        host="localhost"
    )
