from entity.reservation_room import ReservationRoom
from database.neo4jdb import Neo4JDB


class ReservationRoomRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, reservation_room: ReservationRoom):
        query = ("MATCH (rm:room {roomID: toInteger($roomID)}) MATCH (r:reservation {reservationID: toInteger("
                 "$reservationID)}) CREATE (r)-[:HAS_RESERVATION]->(rm)")
        self.db.session.run(query, parameters={'roomID': reservation_room.id_room, 'reservationID': reservation_room.id_reservation})
        return

    def list(self):
        query = ("MATCH (rr:reservation)-[r:HAS_RESERVATION]->(rm:room) RETURN rr.reservationID, rm.roomID LIMIT 50")
        result = self.db.session.run(query)
        return result.values()

    def delete(self, reservation_room: ReservationRoom):
        query = "MATCH (rr:reservation {reservationID: toInteger($reservationID)})-[r:HAS_RESERVATION]->(rm:room {roomID: toInteger($roomID)}) DELETE r"
        self.db.session.run(query, parameters={'reservationID': reservation_room.id_reservation,  'roomID': reservation_room.id_room})
        return

    def delete_by_reservation_id(self, id: int):
        query = ("MATCH (rr:reservation {reservationID: toInteger($reservationID)})-[r:HAS_RESERVATION]->(rm:room) "
                 "DELETE r")
        self.db.session.run(query, parameters={'reservationID': id})
        return

