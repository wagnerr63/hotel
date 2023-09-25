from entity.client import Client
from repository.client import ClientRepository


class ClientHandler:
    repository: ClientRepository = None

    def __init__(self):
        clientRepo = ClientRepository()
        self.repository = clientRepo

    def showClientOptions(self):
        print("CLIENTES")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Atualizar")
        print("0 - Voltar")


    def handleOption(self, option: int):
        if option == 1:
            newClient = Client.new()
            print("Informe os dados do cliente:\n")
            print("Nome:")
            newClient.name = input()
            print("CPF:")
            newClient.cpf = input()
            print("Email:")
            newClient.email = input()
            print("Telefone:")
            newClient.phone = input()
            print("Data de nascimento (YYYY-MM-DD):")
            newClient.birth_date = input()

            self.repository.insert(newClient)
            print("Cliente inserido com sucesso!")

        if option == 2:
            print("Clientes: ")
            allClients = self.repository.list()
            for client in allClients:
                print(client)

        if option == 3:
            print("Informe o ID do cliente: ")
            id = input()
            self.repository.delete(id)
            print("Cliente excluido com sucesso!")

        if option == 4:
            print("Informe o ID do cliente: ")
            id = input()
            clientByID = self.repository.findByID(id)

            print("Nome atual é '"+clientByID.name+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo nome: ")
                clientByID.name = input()

            print("Telefone atual é '"+clientByID.phone+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo telefone: ")
                clientByID.phone = input()

            print("E-mail atual é '"+clientByID.email+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo email: ")
                clientByID.email = input()

            print("Data de nascimento atual é '"+str(clientByID.birth_date)+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova data de nascimento (YYYY-MM-DD): ")
                clientByID.birth_date = input()

            print("CPF atual é '"+clientByID.cpf+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo cpf:")
                clientByID.cpf = input()

            self.repository.update(clientByID)
            print("Cliente atualizado com sucesso!")