from typing import Type

from entity.room import Room
from database.neo4jdb import Neo4JDB


class RoomRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, room: Room):
        query = "CREATE (n:room {id:$id, name:$name, qty_beds:$qty_beds, qty_restrooms:$qty_restrooms, hydromassage:$hydromassage, description:$description, price:$price})" 
        self.db.session.run(query, parameters={'id': room.id, 'name': room.name, 'qty_beds': room.qty_beds, 'qty_restrooms': room.qty_restrooms, 'hydromassage': room.hydromassagem, 'description': room.description, 'price': room.price})

    def list(self):
        query = "MATCH (n:room) RETURN n.id, n.name, n.qty_beds, n.qty_restrooms, n.hydromassage, n.description, n.price LIMIT 100"
        results = self.db.session.run(query)
        rooms = results.values()
        return rooms
    
    def delete(self, id: str):
        query = "MATCH (n:room {id:$id}) DELETE n"
        self.db.session.run(query, parameters={'id': id})

    def update(self, room: Room):
        query = "MATCH (n:room {id:$id}) SET n.name=$name, n.qty_beds=$qty_beds, n.qty_restrooms=$qty_restrooms, n.hydromassage=$hydromassage, n.description=$description, n.price=$price"
        self.db.session.run(query, parameters={'id': id, 'name': room.name, 'qty_beds': room.qty_beds, 'qty_restrooms': room.qty_restrooms, 'hydromassage': room.hydromassage, 'description': room.description, 'price': room.price})

    def find_by_id(self, id: str) -> Type[Room]:
        query = "MATCH (n:room {id:$id}) RETURN n.id, n.name, n.description, n.qty_beds, n.qty_restrooms, n.hydromassage, n.price"
        result = self.db.session.run(query, parameters={'id': id})
        row = result.values()[0]

        roomByID = Room
        roomByID.id = row[0]
        roomByID.name = row[1]
        roomByID.description = row[2]
        roomByID.qty_beds = row[3]
        roomByID.qty_restrooms = row[4]
        roomByID.hydromassage = row[5]
        roomByID.price = row[6]
        return roomByID
