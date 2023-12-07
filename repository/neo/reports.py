from database.db import Database

class ReportsRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def select_spent_by_client(self, id_client):
        return
 
    def select_count_reservations_by_client(self, id_client):
        return

    def select_count_activities_by_client(self, id_client):
        return
    
