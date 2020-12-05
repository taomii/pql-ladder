import logging
from charly.modules.APICaller import APIHandler
from charly.modules.DBConnector import DBConnector


api = APIHandler()
db = DBConnector()

playerList = api.call()
db.write(playerList)
