from entity.client import Client
from database.db import Database


class ClientRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, client: Client):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO client(name, phone, email, birth_date, cpf) VALUES(%s, %s, %s, %s, %s);",
            (client.name, client.phone, client.email, client.birth_date, client.cpf))
        self.db.conn.commit()

        cursor.close()

    def list(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM client;")
        clients = cursor.fetchall()
        cursor.close()
        return clients
    

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM client WHERE id = %s",(id))
        self.db.conn.commit()

        cursor.close()

    def update(self, client: Client):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "UPDATE client SET name = %s, phone = %s, email = %s, birth_date = %s, cpf = %s WHERE id = %s;",
            (client.name, client.phone, client.email, client.birth_date, client.cpf, client.id))
        self.db.conn.commit()

        cursor.close()

    def findByID(self, id: int) -> Client:
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM client WHERE id = %s;", (id))
        client = cursor.fetchone()
        cursor.close()

        clientByID = Client
        clientByID.id = client[0]
        clientByID.name = client[1]
        clientByID.phone = client[2]
        clientByID.email = client[3]
        clientByID.birth_date = client[4]
        clientByID.cpf = client[5]

        return clientByID