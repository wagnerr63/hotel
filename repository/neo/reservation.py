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
        query = "CREATE (n:reservation {id:$id, id_client:$id_client, date:$date, employee:$employee, description:$description})"
        self.db.session.run(query, parameters={'id': reservation.id, 'id_client': reservation.id_client, 'date': reservation.date,
                                               'employee': reservation.employee, 'description': reservation.description})
        
    def list(self):
        query = "MATCH (n:reservation) RETURN n.id, n.id_client, n.date, n.employee, n.description LIMIT 100"
        results = self.db.session.run(query)
        reservations = results.values()
        return reservations
    
    def delete(self, id:int):
        query = "MATCH (n.reservation {id:$id}) DELETE n"
        self.db.session.run(query, parameters={'id':id})

    def update(self, reservation: Reservation):
        query = "MATCH (n.reservation {id:$id}) SET n.id_client=$id_client, n.date=$date, n.employee=$employee, n.description=$description"
        self.db.session.run(query, parameters={'id': reservation.id, 'id_client': reservation.id_client, 'date': reservation.date,
                                               'employee': reservation.employee, 'description': reservation.description})

    def findByID(self, id: int) -> Type[Reservation]:
        query = "MATCH (n.reservation {id:$id}) RETURN n.id, n.id_client, n.date, n.employee, n.description"
        result = self.db.session.run(query, parameters={'id': id})
        row = result.values()[0]

        reservationByID = Reservation
        reservationByID.id = row[0]
        reservationByID.id_client = row[1]
        reservationByID.date = row[2]
        reservationByID.employee = row[4]
        reservationByID.description = row[5]