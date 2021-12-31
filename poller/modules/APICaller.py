import requests
import json
from modules.Player import Player

class APIHandler:

    def __init__(self):
        self.urls = ['https://qlstats.net/api/server/185.107.96.27:27960/players',
                     'https://qlstats.net/api/server/212.8.249.10:27961/players']
    def call(self):
        """Calls QLstats API, converts the JSON Data into a dictionary and returns a list of Player """
        playerList = []

        for url in self.urls:
            response = requests.get(url)
            dict_response = json.loads(response.content)

            if dict_response["ok"] == True:
                for playerEntry in dict_response["players"]:
                    if "rating" in playerEntry and playerEntry["rating"] != 0:
                        player = Player(id = playerEntry["steamid"], name = playerEntry['name'], rating = playerEntry["rating"])
                        playerList.append(player)

        return playerList