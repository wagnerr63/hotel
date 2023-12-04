from typing import Type

from entity.client import Client
from database.neo4jdb import Neo4JDB


class ClientRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, client: Client):
        query = "CREATE (n:client {id:$id, name:$name, phone:$phone, email:$email, birth_date:$birth_date, cpf:$cpf})"
        self.db.session.run(query, parameters={'id': client.id, 'name': client.name, 'phone': client.phone,
                                               'email': client.email, 'birth_date': client.birth_date,
                                               'cpf': client.cpf})

    def list(self):
        query = "MATCH (n:client) RETURN n.id, n.name, n.phone, n.email, n.birth_date, n.cpf LIMIT 100"
        results = self.db.session.run(query)
        clients = results.values()
        return clients

    def delete(self, id: int):
        query = "MATCH (n:client {id:$id}) DELETE n"
        self.db.session.run(query, parameters={'id': id})

    def update(self, client: Client):
        query = "MATCH (n:client {id:$id}) SET n.name=$name, n.phone=$phone, n.email=$email, n.birth_date=$birth_date, n.cpf=$cpf"
        self.db.session.run(query, parameters={'id': client.id, 'name': client.name, 'phone': client.phone,
                                               'email': client.email, 'birth_date': client.phone, 'cpf': client.cpf})

    def findByID(self, id: int) -> Type[Client]:
        query = "MATCH (n:client {id:$id}) RETURN n.id, n.name, n.phone, n.email, n.birth_date, n.cpf"
        result = self.db.session.run(query, parameters={'id': id})
        row = result.values()[0]

        clientByID = Client
        clientByID.id = row[0]
        clientByID.name = row[1]
        clientByID.phone = row[2]
        clientByID.email = row[3]
        clientByID.birth_date = row[4]
        clientByID.cpf = row[5]

        return clientByID
