from database.db import Database

class ReportsRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def select_spent_by_client(self, id_client):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "SELECT SUM(rm.price) AS total_spent FROM client AS c LEFT JOIN reservation AS r ON c.id = r.id_client LEFT JOIN reservation_room AS rr ON r.id = rr.id_reservation LEFT JOIN room AS rm ON rr.id_room = rm.id WHERE c.id =  %s;", (id_client,)
            )
        total = cursor.fetchone()
        cursor.close()

        return total
 
    def select_count_reservations_by_client(self, id_client):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "SELECT COUNT(r.id) AS total_stays FROM client AS c LEFT JOIN reservation AS r ON c.id = r.id_client WHERE c.id = %s;", (id_client,)
            )
        total = cursor.fetchone()
        cursor.close()

        return total

    def select_count_activities_by_client(self, id_client):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "SELECT COUNT(ca.id) AS total_activities FROM client AS c LEFT JOIN client_activity AS ca ON c.id = ca.id_client WHERE c.id = %s;", (id_client,)
            )
        total = cursor.fetchone()
        cursor.close()

        return total
    
