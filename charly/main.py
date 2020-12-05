import logging
from charly.modules.APICaller import APIHandler
from charly.modules.DBConnector import DBConnector

#create API Caller
api = APIHandler()
db = DBConnector()

#do things
playerList = api.call()
db.write(playerList)
