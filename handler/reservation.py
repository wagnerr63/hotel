from repository.reservation import ReservationRepository
from entity.reservation import Reservation


class ReservationHandler:
    repository: ReservationRepository = None

    def __init__(self):
        reservationRepo = ReservationRepository()
        self.repository = reservationRepo

    def showReservationOptions(self):
        print("1 - Criar reserva")
        print("2 - Listar reserva")
        print("3 - Excluir reserva")
        print("4 - Atualizar reserva")

    def handleOption(self, option: int):
        if option == 1:
            newReservation = Reservation.new()
            print("Informe os dados da reserva:\n")
            print("ID do cliente:")
            newReservation.id_client = input()
            print("Nome:")
            newReservation.name = input()
            print("Data:")
            newReservation.date = input()
            print("Funcionário:")
            newReservation.employer = input()
            print("Descrição:")
            newReservation.description = input()

            self.reservationRepo.insert(newReservation)
            print("Reserva inserida com sucesso!")

        if option == 2:
            print("Reservas: ")
            allreservation = self.reservationRepo.list()
            for reservations in allreservation:
                print(reservation)

            if option == 3:
                print("Informe o ID da reserva: ")
                id = input()
                self.reservationRepo.delete(id)
                print("Reserva excluida com sucesso!")

            if option == 4:
                print("Informe o ID da reserva: ")
                id = input()
                reservationByID = self.repository.findByID(id)

                print("ID do cliente atual é '"+reservationByID.id_client+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Novo ID do cliente: ")
                    reservationByID.id_client = input()

                print("Nome atual é '"+reservationByID.name+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Novo nome: ")
                    reservationByID.name = input()

                print("Data atual é '"+reservationByID.date+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Nova data: ")
                    reservationByID.date = input()

                print("Funcionário atual é '"+reservationByID.employer+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Novo funcionário: ")
                    reservationByID.employer = input()

                print("Descrição atual é '"+reservationByID.description+"'. Deseja atualizar? (1 - SIM, 0 - Não)")
                opt = int(input())
                if opt == 1:
                    print("Nova descrição:")
                    reservationByID.description = input()

                self.repository.update(reservationByID)
                print("Reserva atualizado com sucesso!")

