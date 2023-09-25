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
            "INSERT INTO room(name, qty_beds, qty_restrooms, hydromassage, description, price) VALUES(%s, %s, %s, %s, %s, %s);",
            (room.name, room.qty_beds, room.qty_restrooms, room.hidromassagem, room.description, room.price))
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

    def findByID(self, id: int) -> Room:
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM room WHERE id = %s;", (id))
        client = cursor.fetchone()
        cursor.close()

        roomByID = Room
        roomByID.id = client[0]
        roomByID.name = client[1]
        roomByID.description = client[2]
        roomByID.qty_beds = client[3]
        roomByID.qty_restrooms = client[4]
        roomByID.hidromassagem = client[5]
        roomByID.price = client[6]
 
        return roomByID