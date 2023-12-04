import uuid


class Client:
    id: str = ""
    name: str = ""
    email: str = ""
    phone: str = ""
    birth_date: str = ""
    cpf: str = ""

    @staticmethod
    def new():
        client = Client
        client.id = uuid.uuid4().__str__()

        return client
