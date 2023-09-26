from typing import Type

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
        cursor.execute("SELECT * FROM activity LIMIT 50;")
        clients = cursor.fetchall()
        cursor.close()
        return clients

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM activity WHERE id = %s", (id))
        self.db.conn.commit()

        cursor.close()

    def find_by_id(self, id: int) -> Type[Activity]:
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM activity WHERE id = %s;", (id))
        client = cursor.fetchone()
        cursor.close()

        if client is None:
            raise NameError("not_found")

        activity_by_id = Activity
        activity_by_id.id = client[0]
        activity_by_id.name = client[1]
        activity_by_id.description = client[2]
        activity_by_id.local = client[3]

        return activity_by_id

    def update(self, activity: Activity):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "UPDATE activity SET name = %s, description = %s, local = %s WHERE id = %s;",
            (activity.name, activity.description, activity.local, activity.id))
        self.db.conn.commit()

        cursor.close()