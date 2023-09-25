from database.db import Database
from repository.client import ClientRepository
from repository.activity import ActivityRepository
from repository.room import RoomRepository
from entity.activity import Activity
from entity.client import Client
from entity.room import Room

if __name__ == '_main_':
    db = Database()
    db.connect()

    clientRepo = ClientRepository()
    activityRepo = ActivityRepository()
    roomRepo = RoomRepository()

    option = -1
    while option != 0:
        print("1 - Criar cliente")
        print("2 - Listar clientes")
        print("3 - Excluir cliente")
        print("4 - Atualizar cliente")
        print("5 - Criar atividade")
        print("6 - Listar atividades")
        print("7 - Excluir atividade")
        print("8 - Atualizar atividade")
        print("9 - Criar quarto")
        print("0 - Sair")
        option = int(input())

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

            clientRepo.insert(newClient)
            print("Cliente inserido com sucesso!")

        if option == 2:
            print("Clientes: ")
            allClients = clientRepo.list()
            for client in allClients:
                print(client)

        if option == 3:
            print("Informe o ID do cliente: ")
            id = input()
            clientRepo.delete(id)
            print("Cliente excluido com sucesso!")

        if option == 4:
            print("Informe o ID do cliente: ")
            id = input()
            clientByID = clientRepo.findByID(id)
            print(clientByID)

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

            print("Data de nascimento atual é '"+clientByID.birth_date+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova data de nascimento: ")
                clientByID.birth_date = input()

            print("CPF atual é '"+str(clientByID.birth_date)+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova data de nascimento (YYYY-MM-DD): ")
                clientByID.birth_date = input()

            clientRepo.update(clientByID)
            print("Cliente atualizado com sucesso!")

        if option == 5:
            newActivity = Activity.new()
            print("Informe os dados da atividade:\n")
            print("Nome:")
            newActivity.name = input()
            print("Local:")
            newActivity.local = input()
            print("Descrição:")
            newClient.description = input()
            
            activityRepo.insert(newActivity)
            print("Atividade inserido com sucesso!")

        if option == 6:
            print("Atividades: ")
            allActivity = activityRepo.list()
            for activity in allActivity:
                print(activity)

        if option == 7:
            print("Informe o ID da atividade: ")
            id = input()
            activityRepo.delete(id)
            print("Atividade excluido com sucesso!")

        if option == 9:
            newRoom = Room.new()
            print("Informe os dados do quarto:\n")
            print("Quantidade:")
            newActivity.name = input()
            print("Local:")
            newActivity.local = input()
            print("Descrição:")
            newClient.description = input()
            
            activityRepo.insert(newActivity)
            print("Atividade inserido com sucesso!")

        


    print("Saindo...")