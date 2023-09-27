from repository.reports import ReportsRepository
from repository.client import ClientRepository

class ReportsHandler:
    repository: ReportsRepository = None
    client_repository: ClientRepository = None

    def __init__(self):
        self.repository = ReportsRepository()
        self.client_repository = ClientRepository()

    def ReportsOptions(self):
        print("RELATÓRIOS")
        print("1 - Gastos por cliente")
        print("2 - Hospedagens por cliente")
        print("3 - Atividades por clientes")
        print("0 - Voltar")
        option = int(input())

        print("Digite o id do cliente: ")
        id_client = input()
        client = self.client_repository.findByID(id_client)
        print("Cliente: "+client.name)
        
        if option == 1:
            total = self.repository.select_spent_by_client(id_client)
            print("Total gasto pelo cliente no hotel: "+str(total[0]))

        if option == 2:
            total = self.repository.select_count_reservations_by_client(id_client)
            print("Quantidade de reservas realizadas pelo cliente "+str(total[0]))

        if option == 3:
            total = self.repository.select_count_activities_by_client(id_client)
            print("Quantidade de atividade realizadas pelo cliente no hotel "+str(total[0]))