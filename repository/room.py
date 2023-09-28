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
        cursor.execute("SELECT * FROM room LIMIT 50;")
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
        cursor.execute("SELECT * FROM room WHERE id = %s;", (id,))
        room = cursor.fetchone()
        cursor.close()

        if room is None:
            raise NameError("not_found")

        roomByID = Room
        roomByID.id = room[0]
        roomByID.name = room[1]
        roomByID.description = room[2]
        roomByID.qty_beds = room[3]
        roomByID.qty_restrooms = room[4]
        roomByID.hidromassagem = room[5]
        roomByID.price = room[6]
 
        return roomByID

    def update(self, room: Room):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "UPDATE room SET "
            "name = %s, "
            "description = %s, "
            "qty_beds = %s, "
            "qty_restrooms = %s, "
            "hydromassage = %s, "
            "price = %s WHERE id = %s;",
            (room.name, room.description, room.qty_beds, room.qty_restrooms, room.hidromassagem, room.price, room.id))
        self.db.conn.commit()

        cursor.close()