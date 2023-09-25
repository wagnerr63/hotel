
class Room:
    id: int = None
    qty_beds: int = ""
    qty_restrooms: int = ""
    hidromassagem: bool = False
    description: str = ""
    price: float = ""
    name: str = ""

    @staticmethod
    def new():
        room = Room
        
        return room
