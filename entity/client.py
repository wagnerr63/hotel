import uuid


class Client:
    id = None
    name: str = ""
    email: str = ""
    phone: str = ""
    birth_date: str = ""
    cpf: str = ""

    @staticmethod
    def new():
        client = Client

        return client
