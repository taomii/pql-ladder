import configparser
import logging

from charly.modules.APICaller import APIHandler
from charly.modules.DBConnector import DBConnector

def main():
    logger = logging.getLogger(__name__)
    logger.debug("Launching Charly Webapp")

    config = configparser.ConfigParser()
    config.read("../config.ini")

    api = APIHandler()
    db = DBConnector()

    playerList = api.call()
    db.write(playerList)

