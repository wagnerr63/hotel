import psycopg2
from database.db import Database

if __name__ == '__main__':
    db = Database()
    db.connect()

    print("Saindo...")
