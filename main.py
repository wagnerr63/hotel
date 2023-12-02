from database.db import Database
from handler.client import ClientHandler
from handler.activity import ActivityHandler
from handler.reservation import ReservationHandler
from handler.room import RoomHandler
from handler.report import ReportsHandler
from database.neo4jdb import Neo4JDB
from repository.neo.activity import ActivityRepository
from entity.activity import Activity

if __name__ == '__main__':
    print("oi")

    activityRepo = ActivityRepository()
    # newActivity = Activity.new()
    # newActivity.name = "a"
    # newActivity.local = "b"
    # newActivity.description = "c"
    # activityRepo.insert(newActivity)
    activities = activityRepo.list()
    print(activities)
    activityRepo.delete('27909786-49e7-4263-9393-0c2d20b37ad8')
    print(activityRepo.list())



    # clientHandler = ClientHandler()
    # activityHandler = ActivityHandler()
    # reservationHandler = ReservationHandler()
    # roomHandler = RoomHandler()
    # reportHandler = ReportsHandler()

    # option = -1
    # while option != 0:
    #     print("1 - Gerenciar Clientes")
    #     print("2 - Gerenciar Atividades")
    #     print("3 - Gerenciar Reservas")
    #     print("4 - Gerenciar Quartos")
    #     print("5 - Gerar relatórios")
    #     print("0 - Sair")
    #     option = int(input())

    #     if option == 1:
    #         clientHandler.showClientOptions()
    #         opt = int(input())
    #         clientHandler.handleOption(opt)


    #     if option == 2:
    #        activityHandler.showActivityOptions()
    #        opt = int(input())
    #        activityHandler.handleOption(opt)

    #     if option == 3:
    #        reservationHandler.showReservationOptions()
    #        opt = int(input())
    #        reservationHandler.handleOption(opt)

    #     if option == 4:
    #         roomHandler.showRoomOptions()
    #         opt = int(input())
    #         roomHandler.handleOption(opt)
        
    #     if option == 5:
    #         reportHandler.ReportsOptions()

            

    print("Saindo...")