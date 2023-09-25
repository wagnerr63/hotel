from repository.room import RoomRepository
from entity.room import Room

class RoomHandler:
    repository: RoomtRepository = None

    def __init__(self):
        roomRepo = RoomRepository()
        self.repository = roomRepo

    def showRoomOptions(self):
        print("1 - Criar quarto")
        print("2 - Listar quarto")
        print("3 - Excluir quarto")
        print("4 - Atualizar quarto")

    def handleOption(self, option: int)
          if option == 1:
            newRoom = Room.new()
            print("Informe os dados do quarto:\n")
            print("Quantidade de camas:")
            newRoom.qty_beds = input()
            print("Quantidade de banheiros:")
            newRoom.qty_restrooms = input()
            print("Hidromassagem:")
            newRoom.hidromassagem = input()
            print("Descrição:")
            newRoom.description = input()
            print("Valor:")
            newRoom.value = input()

            self.roomRepo.insert(newRoom)
            print("Quarto inserido com sucesso!")

        if option == 2:
            print("Quartos: ")
            allroom = self.roomRepo.list()
            for room in allroom:
                print(room)

        if option == 3:
            print("Informe o ID do quarto: ")
            id = input()
            selfroomRepo.delete(id)
            print("Quarto excluido com sucesso!")

    print("Saindo...")
