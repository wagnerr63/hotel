from repository.postgres.activity import ActivityRepository
from entity.activity import Activity
from entity.client_activity import ClientActivity
from repository.postgres.client_activity import ClientActivityRepository

class ActivityHandler:
    repository: ActivityRepository = None
    clientActivity: ClientActivityRepository = None

    def __init__(self):
        activityRepo = ActivityRepository()
        self.repository = activityRepo
        self.clientActivity = ClientActivityRepository()

    def showActivityOptions(self):
        print("ATIVIDADES")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Atualizar")
        print("5 - Registrar cliente atividade")
        print("6 - Excluir cliente atividade")
        print("0 - Voltar")

    def handleOption(self, option: int):
        if option == 1:
            newActivity = Activity.new()
            print("Informe os dados da atividade:\n")
            print("Nome:")
            newActivity.name = input()
            print("Local:")
            newActivity.local = input()
            print("Descrição:")
            newActivity.description = input()
            try:
                self.repository.insert(newActivity)
            except Exception:
                print("Ocorreu um erro inesperado!")
                return

            print("Atividade inserido com sucesso!")

        if option == 2:
            print("Atividades: ")
            allActivity = self.repository.list()
            print("ID | Nome | Descricão | Local ")
            for activity in allActivity:
                print(str(activity[0])+" | "+activity[1]+" | "+activity[3]+" | "+activity[2])
            print("--------")

        if option == 3:
            print("Informe o ID da atividade: ")
            id = input()
            try:
                self.repository.delete(id)
            except Exception:
                print("Ocorreu um erro inesperado!")
                return

            print("Atividade excluido com sucesso!")

        if option == 4:
            print("Informe o ID da atividade: ")
            id = input()
            try:
                activityByID = self.repository.find_by_id(id)
            except NameError as e:
                if e.args[0] == "not_found":
                    print("Atividade não encontrada com id "+str(id))
                    return


            print("Nome atual é '"+activityByID.name+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo nome: ")
                activityByID.name = input()

            print("Local atual é '"+activityByID.local+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo local: ")
                activityByID.local = input()

            print("Descrição atual é '"+activityByID.description+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova descrição: ")
                activityByID.email = input()

            self.repository.update(activityByID)
            print("Atividade atualizada com sucesso!")
        
        if option == 5:
            new = ClientActivity
            print("Informe o ID do cliente")
            new.id_client = input()

            print("Informe o ID da atividade")
            new.id_activity = input()
            try:
                self.clientActivity.insert(new)
            except Exception as e:
                print(e)
                print("Ocorreu um erro na operacao")
                return
            
            print("Sucesso!")

        if option == 6:
            print("Informe o ID do cliente")
            id_client = input()

            all = self.clientActivity.list_all_by_client(id_client)
            print("ID | Nome | Data ")
            for activity in all:
                print(activity)

            print("Informe o ID da atividade que deseja excluir")
            id_activity = input()
            try:
                self.clientActivity.delete(id_activity)
            except Exception as e:
                print(e)
                print("Ocorreu um erro na operacao")
                return
            
            print("Sucesso!")
            

