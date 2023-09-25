from entity.reservation_room import ReservationRoom
from database.db import Database


class ReservationRoomRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, reservation_room: ReservationRoom):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO reservation_room(id_room, id_reservation) VALUES(%s, %s);",
            (reservation_room.id_room, reservation_room.id_reservation))
        self.db.conn.commit()

        cursor.close()

    def list(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM reservation_room;")
        clients = cursor.fetchall()
        cursor.close()
        return clients
    

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM reservation_room WHERE id = %s",(id))
        self.db.conn.commit()

        cursor.close()