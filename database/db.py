import psycopg2


class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = "root"
        self.port = "5432"
        self.dbname = "hotel"
        self.conn = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as e:
                raise e