from typing import Type

import neo4j.exceptions

from entity.activity import Activity
from database.neo4jdb import Neo4JDB


class ActivityRepository:
    db: Neo4JDB = None

    def __init__(self):
        db = Neo4JDB()
        self.db = db
        self.db.connect()

    def insert(self, activity: Activity):
        last_id = self.find_last_id()
        activityID = last_id+1
        query = "CREATE (n:activity {activityID:$activityID, name:$name, local:$local, description:$description})"
        self.db.session.run(query, parameters={'activityID': activityID, 'name': activity.name, 'local': activity.local,
                                               'description': activity.description})

    def find_last_id(self) -> int:
        query = "match (n:activity) return n.activityID ORDER BY n.activityID DESC LIMIT 1"
        result = self.db.session.run(query)
        if not result.peek():
            return 0
        return int(result.single()[0])


    def list(self):
        query = "MATCH (n:activity) RETURN n.activityID, n.name, n.local, n.description LIMIT 100"
        results = self.db.session.run(query)
        activities = results.values()
        return activities

    def delete(self, id: str):
        query = "MATCH (n:activity {activityID:$id}) DELETE n"
        self.db.session.run(query, parameters={'id': id})

    def update(self, activity: Activity):
        query = "MATCH (n:activity {activityID:$id}) SET n.name=$name, n.local=$local, n.description=$description"
        self.db.session.run(query, parameters={'id': activity.id, 'name': activity.name, 'local': activity.local,
                                               'description': activity.description})

    def find_by_id(self, id: str) -> Type[Activity]:
        query = "MATCH (n:activity {activityID: $id}) RETURN n.id, n.name, n.local, n.description"
        result = self.db.session.run(query, parameters={'id': id})
        row = result.values()[0]

        activityByID = Activity
        activityByID.id = row[0]
        activityByID.name = row[1]
        activityByID.local = row[2]
        activityByID.description = row[3]
        return activityByID

