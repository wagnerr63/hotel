from repository.postgres.room import RoomRepository
from entity.room import Room

class RoomHandler:
    repository: RoomRepository = None

    def __init__(self):
        roomRepo = RoomRepository()
        self.repository = roomRepo

    def showRoomOptions(self):
        print("QUARTOS")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Atualizar")

    def handleOption(self, option: int):
        if option == 1:
            newRoom = Room.new()
            print("Informe os dados do quarto:\n")
            print("Nome: ")
            newRoom.name = input()
            print("Quantidade de camas:")
            newRoom.qty_beds = input()
            print("Quantidade de banheiros:")
            newRoom.qty_restrooms = input()
            print("Possui hidromassagem?: (1- Sim, 0 - Não)")
            hidro = int(input())
            if hidro == 1:
                newRoom.hidromassagem = True
            else:
                newRoom.hidromassagem = False
            print("Descrição:")
            newRoom.description = input()
            print("Valor:")
            newRoom.price = input()

            try:
                self.repository.insert(newRoom)
                print("Quarto inserido com sucesso!")
            except Exception as e:
                print(e)
                print("Ocorreu um erro na operação")

        if option == 2:
            print("Quartos")
            print("ID | Nome | Descricão | Qtd Camas | Qtd Banheiros | Possui hidromassagem | Valor")
            try:
                allrooms = self.repository.list()
                for room in allrooms:
                    print(str(room[0])+" | "+room[1]+" | "+str(room[2])+" | "+str(room[3])+" | "+str(room[4])+" | "+str(room[5])+" | "+str(room[6]))
            except Exception as e:
                print(e)
                print("Ocorreu um erro")

        if option == 3:
            print("Informe o ID do quarto: ")
            id = input()
            try:
                self.repository.delete(id)
                print("Quarto excluido com sucesso!")
            except Exception as e:
                print(e)
                print("Ocorreu um erro")

        if option == 4:
            print("Informe o ID do quarto: ")
            id = input()
            try:
                roomByID = self.repository.findByID(id)
            except NameError as e:
                if e.args[0] == "not_found":
                    print("Quarto não encontrado com id "+id)
                    return

            print("Nome atual é '"+roomByID.name+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo nome: ")
                roomByID.name = input()

            print("Quantidade de camas atual é '"+str(roomByID.qty_beds)+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova quantidade de camas: ")
                roomByID.qty_beds = input()

            print("Quantidade de banheiros atual é '"+str(roomByID.qty_restrooms)+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova quantidade de banheiros: ")
                roomByID.qty_restrooms = input()

            print("Valor de hidromassagem atual é '"+str(roomByID.hidromassagem)+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo valor de hidromassagem (1 - Sim, 0 Não): ")
                hidro = int(input())
                if hidro == 1:
                    roomByID.hidromassagem = True
                else:
                    roomByID.hidromassagem = False

            print("Descrição atual é '"+roomByID.description+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Nova descrição: ")
                roomByID.description = input()

            print("Valor atual é '"+str(roomByID.price)+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
            opt = int(input())
            if opt == 1:
                print("Novo valor:")
                roomByID.price = input()

            try:
                self.repository.update(roomByID)
                print("Quarto atualizado com sucesso!")
            except Exception as e:
                print(e)
                print("Ocorreu um erro")

