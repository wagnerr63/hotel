from entity.room import Room
from database.db import Database


class RoomRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, room: Room):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO room(qty_beds, qty_restrooms, hidromassagem, description, value) VALUES(%s, %s, %s, %s, %s);",
            (room.qty_beds, room.qty_restrooms, room.hidromassagem, room.description, room.value))
        self.db.conn.commit()

        cursor.close()

    def list(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM room;")
        clients = cursor.fetchall()
        cursor.close()
        return clients
    

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM room WHERE id = %s",(id))
        self.db.conn.commit()

        cursor.close()