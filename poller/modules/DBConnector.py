import sqlite3
import psycopg2
import os

class DBConnector:
    def writePlayers(self, playerList):
        conn = psycopg2.connect(
            host="localhost",
            database="charly",
            user="postgres",
            password="postgres",
            port='5432')

        cursor = conn.cursor()
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
        print("hello")

    def write(self, playerList):

        """To rewrite in """
        conn = sqlite3.connect('../ranking.db')
        c = conn.cursor()

        for player in playerList:
            c.execute("SELECT * FROM players WHERE id =" + player.id)
            result = c.fetchone()

            # Add new found Player
            if result == None:
                c.execute("INSERT INTO players VALUES (?, ?, ?)", (player.id, player.name, player.rating))

            # Update Name or Rating, if necessary
            else:
                if str(result[1]) != str(player.name):
                    c.execute("UPDATE players SET nickname ='" + player.name + "' WHERE id =" + player.id)
                if int(result[2]) != int(player.rating):
                    c.execute("UPDATE players SET elo =" + player.rating + " WHERE id =" + player.id)
            conn.commit()

        c.close()
        conn.close()