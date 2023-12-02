from neo4j import GraphDatabase


class Neo4JDB:
    def __init__(self):
        self.uri = "bolt://localhost:7687"
        self.user = "neo4j"
        self.password = "12345678"
        self.dbname = "hotel"
        self.driver = None
        self.session = None

    def connect(self):
        if self.driver is None and self.session is None:
            try:
                self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
                self.session = self.driver.session()
            except Exception as e:
                raise e

    def close(self):
        self.session.close()
        self.driver.close()
