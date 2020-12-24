from charly.modules.APICaller import APIHandler
from charly.modules.DBConnector import DBConnector
from charly.modules.util import Context

def task(ctx: Context):
    api = APIHandler()
    db = DBConnector()

    ctx.logger.debug("Making API call")
    playerList = api.call()

    ctx.logger.debug("Writing data to DB")
    db.write(playerList)