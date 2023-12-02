from entity.activity import Activity
from database.neo4jdb import Neo4JDB


class ActivityRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, activity: Activity):
        query = "CREATE (n:activity {id:$id, name:$name, local:$local, description:$description})"
        self.db.session.run(query, parameters={'id': activity.id, 'name': activity.name, 'local': activity.local,
                                               'description': activity.description})

    def list(self):
        query = "MATCH (n:activity) RETURN n.id, n.name, n.local, n.description LIMIT 100"
        results = self.db.session.run(query)
        activities = results.values()
        return activities

    def delete(self, id: str):
        query = "MATCH (n:activity {id:$id}) DELETE n"
        self.db.session.run(query, parameters={'id': id})
