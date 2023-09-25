from repository.activity import ActivityRepository
from entity.activity import Activity

class ActivityHandler:
    repository: ActivityRepository = None

    def __init__(self):
        activityRepo = ActivityRepository()
        self.repository = activityRepo

    def showActivityOptions(self):
        print("1 - Criar atividade")
        print("2 - Listar atividades")
        print("3 - Excluir atividade")
        print("4 - Atualizar atividade")

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
            
            self.activityRepo.insert(newActivity)
            print("Atividade inserido com sucesso!")

        if option == 2:
            print("Atividades: ")
            allActivity = self.activityRepo.list()
            for activity in allActivity:
                print(activity)

        if option == 3:
            print("Informe o ID da atividade: ")
            id = input()
            self.activityRepo.delete(id)
            print("Atividade excluido com sucesso!")

        if option == 4:
            print("Informe o ID da atividade: ")
            id = input()
            activityByID = self.repository.findByID(id)

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
