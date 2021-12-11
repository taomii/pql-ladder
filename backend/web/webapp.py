from flask import Flask
from flask_table import Table, Col
import sqlite3

from charly.modules.Player import Player

def launch(config):

    app = Flask(__name__)
    app.config["DEBUG"] = True

    class PlayerTable(Table):
        name = Col('Name')
        rating = Col('Elo')
        id = Col('id')

    @app.route('/')
    def mainpage():

        conn = sqlite3.connect('../ranking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM players")
        result = c.fetchall()
        c.close()
        conn.close()

        playerList = []
        for playerEntry in result:
            (id, name, rating) = playerEntry
            player = Player(id, name, rating)
            playerList.append(player)

        playerList.sort(key=lambda x: int(x.rating), reverse=True)
        table = PlayerTable(playerList)

        return table.__html__()

    @app.route('/player/<username>')
    def show_player_profile(username):
        # show the user profile for that user
        return f'User {username}'

    app.run()