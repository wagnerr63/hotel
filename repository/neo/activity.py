from typing import Type

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

    def find_by_id(self, id: str) -> Type[Activity]:
        query = "MATCH (n:activity {id:$id}) RETURN n.id, n.name, n.local, n.description"
        result = self.db.session.run(query, parameters={'id': id})
        row = result.values()[0]

        activityByID = Activity
        activityByID.id = row[0]
        activityByID.name = row[1]
        activityByID.local = row[2]
        activityByID.description = row[3]
        return activityByID

