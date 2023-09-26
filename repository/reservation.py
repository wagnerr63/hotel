from entity.reservation import Reservation
from database.db import Database


class ReservationRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, reservation: Reservation):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO reservation(id_client, name, date, employer, description) VALUES(%s, %s, %s, %s, %s);",
            (reservation.id_client, reservation.name, reservation.date, reservation.employer, reservation.description))
        self.db.conn.commit()

        cursor.close()

    def list(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM reservation LIMIT 50;")
        clients = cursor.fetchall()
        cursor.close()
        return clients
    

    def delete(self, id: int):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "DELETE FROM reservation WHERE id = %s",(id))
        self.db.conn.commit()

        cursor.close()