from repository.activity import ActivityRepository
from entity.activity import Activity

class ActivityHandler:
    repository: ActivityRepository = None

    def __init__(self):
        activityRepo = ActivityRepository()
        self.repository = activityRepo

    def showActivityOptions(self):
        print("ATIVIDADES")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Atualizar")
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
            
            self.repository.insert(newActivity)
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
            self.repository.delete(id)
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
