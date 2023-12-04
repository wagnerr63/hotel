import uuid

class Room:
    id: str = None
    qty_beds: int = ""
    qty_restrooms: int = ""
    hydromassage: bool = False
    description: str = ""
    price: float = ""
    name: str = ""

    @staticmethod
    def new():
        room = Room
        room.id = uuid.uuid4().__str__()

        
        return room
