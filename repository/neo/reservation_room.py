from entity.reservation_room import ReservationRoom
from database.neo4jdb import Neo4JDB


class ReservationRoomRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, reservation_room: ReservationRoom):
        return

    def list(self):
        return

    def delete(self, id: int):
        return

    def delete_by_reservation_id(self, id: int):
        return

