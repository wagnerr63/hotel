from repository.room import RoomRepository
from entity.room import Room

class RoomHandler:
    repository: RoomRepository = None

    def __init__(self):
        roomRepo = RoomRepository()
        self.repository = roomRepo

    def showRoomOptions(self):
        print("1 - Criar quarto")
        print("2 - Listar quarto")
        print("3 - Excluir quarto")
        print("4 - Atualizar quarto")

    def handleOption(self, option: int):
        if option == 1:
            newRoom = Room.new()
            print("Informe os dados do quarto:\n")
            print("Quantidade de camas:")
            newRoom.qty_beds = input()
            print("Quantidade de banheiros:")
            newRoom.qty_restrooms = input()
            print("Hidromassagem:")
            newRoom.hidromassagem = bool(input())
            print("Descrição:")
            newRoom.description = input()
            print("Valor:")
            newRoom.price = input()

            self.repository.insert(newRoom)
            print("Quarto inserido com sucesso!")

        if option == 2:
            print("Quartos: ")
            allroom = self.repository.list()
            for room in allroom:
                print(room)

            if option == 3:
                print("Informe o ID do quarto: ")
                id = input()
                self.repository.delete(id)
                print("Quarto excluido com sucesso!")

            if option == 4:
                print("Informe o ID do quarto: ")
                id = input()
                roomByID = self.repository.findByID(id)

                print("Quantidade de camas atual é '"+roomByID.qty_beds+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Nova quantidade de camas: ")
                    roomByID.qty_beds = input()

                print("Quantidade de banheiros atual é '"+roomByID.qty_restrooms+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Nova quantidade de banheiros: ")
                    roomByID.qty_restrooms = input()

                print("Valor de hidromassagem atual é '"+roomByID.hidromassagem+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Novo valor de hidromassagem: ")
                    roomByID.hidromassagem = input()

                print("Descrição atual é '"+roomByID.description+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Nova descrição: ")
                    roomByID.description = input()

                print("Valor atual é '"+roomByID.price+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Novo valor:")
                    roomByID.price = input()

                self.repository.update(roomByID)
                print("Quarto atualizado com sucesso!")

