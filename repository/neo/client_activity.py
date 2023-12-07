from entity.client_activity import ClientActivity
from database.neo4jdb import Neo4JDB


class ClientActivityRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, client_activity: ClientActivity):
        query = ("MATCH (c:client {clientID: toInteger($clientID)}) MATCH (a:activity {activityID: toInteger("
                 "$activityID)}) CREATE (c)-[:HAS_ACTIVITY]->(a)")
        self.db.session.run(query, parameters={'clientID': client_activity.id_client, 'activityID': client_activity.id_activity})
        return
    def list(self):
        query = ("MATCH (c:client)-[r:HAS_ACTIVITY]->(a:activity) RETURN c.clientID, a.activityID LIMIT 50")
        result = self.db.session.run(query)
        return result.values()
    

    def delete(self, id: int, client_id):
        query = ("MATCH (c:client {clientID: toInteger($clientID)})-[r:HAS_ACTIVITY]->(a:activity {activityID: toInteger($activityID)}) "
                 "DELETE r")
        self.db.session.run(query, parameters={'clientID': client_id, 'activityID': id})
        return

    def delete_by_client_id(self, id: int):
        query = ("MATCH (c:client {clientID: toInteger($clientID)})-[r:HAS_ACTIVITY]->(a:activity) "
                 "DELETE r")
        self.db.session.run(query, parameters={'clientID': id})
        return


    def list_all_by_client(self, id_client):
        query = "MATCH (c:client {clientID: toInteger($clientID)})-[r:HAS_ACTIVITY]->(a:activity) RETURN a.activityID, a.name, a.date LIMIT 50"
        results = self.db.session.run(query, parameters={'clientID': id_client})
        return results.values()
