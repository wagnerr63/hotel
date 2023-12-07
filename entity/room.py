import uuid

class Room:
    id = None
    qty_beds: int = ""
    qty_restrooms: int = ""
    hydromassage: bool = False
    description: str = ""
    price: float = ""
    name: str = ""

    @staticmethod
    def new():
        room = Room

        
        return room
