
class Reservation:
    id: int = None
    id_client: int = ""
    date: str = ""
    employee: str = ""
    description: str = ""

    @staticmethod
    def new():
        reservation = Reservation
        
        return reservation
