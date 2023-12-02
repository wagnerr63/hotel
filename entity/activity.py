import uuid


class Activity:
    id: str = None
    name: str = ""
    local: str = ""
    description: str = ""

    @staticmethod
    def new():
        activity = Activity
        activity.id = uuid.uuid4().__str__()
        
        return activity
