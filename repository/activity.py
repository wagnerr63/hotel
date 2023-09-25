from entity.activity import Activity
from database.db import Database


class ActivityRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, activity: Activity):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO activity(name, local, description) VALUES(%s, %s, %s);",
            (activity.name, activity.local, activity.description))
        self.db.conn.commit()

        cursor.close()

    def list(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM activity;")
        clients = cursor.fetchall()
        cursor.close()
        return clients
    

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM activity WHERE id = %d",(id))
        self.db.conn.commit()

        cursor.close()
        