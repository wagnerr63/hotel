
class Reservation:
    id: int = None
    id_client: int = ""
    name: str = ""
    date: str = ""
    employer: str = "" 
    description: str = ""

    @staticmethod
    def new():
        reservation = Reservation
        
        return reservation
