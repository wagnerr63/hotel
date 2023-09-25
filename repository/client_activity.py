from entity.client_activity import ClientActivity
from database.db import Database


class ClientActivityRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, client_activity: ClientActivity):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO client_activity(id_activity, id_client) VALUES(%s, %s);",
            (client_activity.id_activity, client_activity.id_client))
        self.db.conn.commit()

        cursor.close()

    def list(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM client_activity;")
        clients = cursor.fetchall()
        cursor.close()
        return clients
    

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM client_activity WHERE id = %s",(id))
        self.db.conn.commit()

        cursor.close()