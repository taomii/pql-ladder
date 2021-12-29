from time import sleep

from modules.APICaller import APIHandler
from modules.DBConnector import DBConnector

def main():
    #Setup, maybe read from config file to read intervall, servers etc.
    api = APIHandler()
    db = DBConnector()

    while(True):
        playerList = api.call()
        db.writePlayers(playerList)
        sleep(10)

if __name__ == "__main__":
    main()