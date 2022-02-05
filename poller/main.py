import traceback

from time import sleep

from modules.APICaller import APIHandler
from modules.DBConnector import DBConnector

def main():
    #Setup, maybe read from config file to read intervall, servers etc.
    api = APIHandler()
    db = DBConnector()

    while(True):
        try:
            playerList = api.call()
            db.writePlayers(playerList)
        except Exception as e:
            print("Error XD \n" + traceback.format_exc())
            continue
        sleep(15)

if __name__ == "__main__":
    main()