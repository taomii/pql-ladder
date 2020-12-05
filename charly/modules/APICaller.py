import requests
import json
from charly.modules.Player import Player

class APIHandler:

    def __init__(self):
        self.url = 'https://qlstats.net/api/server/185.107.96.27:27960/players'

    def call(self):
        """Calls QLstats API, converts the JSON Data into a dictionary and returns a list of Player """
        response = requests.get(self.url)
        dict_response = json.loads(response.content)
        playerList = []

        if dict_response["ok"] == True:
            for playerEntry in dict_response["players"]:
                if "rating" in playerEntry:
                    player = Player(playerEntry["steamid"], playerEntry['name'], playerEntry["rating"])
                    playerList.append(player)

        return playerList

