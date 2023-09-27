from repository.reservation import ReservationRepository
from repository.client import ClientRepository
from repository.room import RoomRepository
from repository.reservation_room import ReservationRoomRepository
from entity.reservation import Reservation
from entity.reservation_room import ReservationRoom
from datetime import datetime


class ReservationHandler:
    repository: ReservationRepository = None
    clientRepository: ClientRepository = None
    roomRepository: RoomRepository = None
    reservationRoomRepository: ReservationRoomRepository = None

    def __init__(self):
        repository = ReservationRepository()
        self.repository = repository
        self.clientRepository = ClientRepository()
        self.roomRepository = RoomRepository()
        self.reservationRoomRepository = ReservationRoomRepository()

    def showReservationOptions(self):
        print("RESERVAS")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Excluir")
        # print("4 - Atualizar")

    def handleOption(self, option: int):
        if option == 1:
            newReservation = Reservation.new()
            print("Informe os dados da reserva:\n")
            valid = False
            while valid is not True:
                print("ID do cliente:")
                newReservation.id_client = input()
                try:
                    self.clientRepository.findByID(newReservation.id_client)
                except NameError as e:
                    if e.args[0] == "not_found":
                        print("Cliente não encontrado com id " + newReservation.id_client + ". Informe novamente")
                else:
                    valid = True

            print("Funcionário:")
            newReservation.employee = input()
            print("Descrição:")
            newReservation.description = input()

            newReservation.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                idReservation = self.repository.insert(newReservation)
            except Exception as e:
                print(e)
                print("Ocorreu um erro ao tentar cadastrar esta reserva")
                return

            print("Quantos quartos deseja reservar?")
            qty_rooms = int(input())

            all_rooms = self.roomRepository.list()
            print("Quartos disponíveis")
            print("ID | Nome | Descricão | Qtd Camas | Qtd Banheiros | Possui hidromassagem | Valor")
            for room in all_rooms:
                print(str(room[0]) + " | " + room[1] + " | " + str(room[2]) + " | " + str(room[3]) + " | " + str(
                    room[4]) + " | " + str(room[5]) + " | " + str(room[6]))

            for i in range(qty_rooms):
                new_reservation_room = ReservationRoom
                new_reservation_room.id_reservation = idReservation
                print("Informe o ID do quarto " + str(i + 1))
                new_reservation_room.id_room = input()
                self.reservationRoomRepository.insert(new_reservation_room)

            print("Reserva inserida com sucesso!")

        if option == 2:
            print("Reservas: ")
            allreservation = self.repository.list()
            for reservation in allreservation:
                print(reservation)

        if option == 3:
            print("Informe o ID da reserva: ")
            teste = input()
            self.reservationRoomRepository.delete(id)
            self.repository.delete(teste)
            print("Reserva excluida com sucesso!")

        # if option == 4:
        #     print("Informe o ID da reserva: ")
        #     id = input()
        #     try:
        #         reservationByID = self.repository.findByID(id)
        #     except NameError as e:
        #         if e.args[0] == "not_found":
        #             print("Reserva não encontrado.")
        #             return
        #
        #     print("ID do cliente atual é '"+reservationByID.id_client+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
        #     opt = int(input())
        #     if opt == 1:
        #         print("Novo ID do cliente: ")
        #         reservationByID.id_client = input()
        #
        #     print("Nome atual é '"+reservationByID.name+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
        #     opt = int(input())
        #     if opt == 1:
        #         print("Novo nome: ")
        #         reservationByID.name = input()
        #
        #     print("Data atual é '"+reservationByID.date+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
        #     opt = int(input())
        #     if opt == 1:
        #         print("Nova data: ")
        #         reservationByID.date = input()
        #
        #     print("Funcionário atual é '"+reservationByID.employer+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
        #     opt = int(input())
        #     if opt == 1:
        #         print("Novo funcionário: ")
        #         reservationByID.employer = input()
        #
        #     print("Descrição atual é '"+reservationByID.description+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
        #     opt = int(input())
        #     if opt == 1:
        #         print("Nova descrição:")
        #         reservationByID.description = input()
        #
        #     self.repository.update(reservationByID)
        #     print("Reserva atualizado com sucesso!")
