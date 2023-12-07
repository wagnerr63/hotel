from typing import Type

from entity.reservation import Reservation
from database.neo4jdb import Neo4JDB


class ReservationRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, reservation: Reservation):
        last_id = self.find_last_id()
        reservation.id = last_id + 1
        query = "CREATE (n:reservation {reservationID:$reservationID, id_client:$id_client, date:$date, employee:$employee, description:$description})"
        self.db.session.run(query, parameters={'reservationID': reservation.id, 'id_client': reservation.id_client,
                                               'date': reservation.date,
                                               'employee': reservation.employee,
                                               'description': reservation.description})

        return reservation.id

    def find_last_id(self) -> int:
        query = "match (n:reservation) return n.reservationID ORDER BY n.reservationID DESC LIMIT 1"
        result = self.db.session.run(query)
        if not result.peek():
            return 0
        return int(result.single()[0])

    def list(self):
        query = "MATCH (n:reservation) RETURN n.reservationID, n.id_client, n.date, n.employee, n.description LIMIT 100"
        results = self.db.session.run(query)
        reservations = results.values()
        return reservations

    def delete(self, id: int):
        query = "MATCH (n:reservation {reservationID:toInteger($id)}) DELETE n"
        self.db.session.run(query, parameters={'id': id})

    def update(self, reservation: Reservation):
        query = "MATCH (n.reservation {reservationID:toInteger($id)}) SET n.id_client=$id_client, n.date=$date, n.employee=$employee, n.description=$description"
        self.db.session.run(query, parameters={'id': reservation.id, 'id_client': reservation.id_client,
                                               'date': reservation.date,
                                               'employee': reservation.employee,
                                               'description': reservation.description})

    def findByID(self, id: int) -> Type[Reservation]:
        query = "MATCH (n.reservation {reservationID:toInteger($id)}) RETURN n.reservationID, n.id_client, n.date, n.employee, n.description"
        result = self.db.session.run(query, parameters={'id': id})
        row = result.values()[0]

        reservationByID = Reservation
        reservationByID.id = row[0]
        reservationByID.id_client = row[1]
        reservationByID.date = row[2]
        reservationByID.employee = row[4]
        reservationByID.description = row[5]

        return reservationByID