import sqlite3
import psycopg2
import os
import datetime

class DBConnector:
    def writePlayers(self, playerList):
        conn = psycopg2.connect(
            host="db",
            database="charly",
            user="postgres",
            password="postgres",
            port='5432')

        c = conn.cursor()

        for player in playerList:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": Player online: " + str(player.id) + " " + player.name + " " +  str(player.rating))

            c.execute("SELECT * FROM players WHERE steamid =" + player.id)
            result = c.fetchone()

            # Add new found Player
            if result == None:
                c.execute("INSERT INTO players VALUES (%s, %s, %s)", (player.id, player.name, player.rating))

            # Update Name or Rating, if necessary
            else:
                if str(result[1]) != str(player.name):
                    c.execute("UPDATE players SET nickname ='" + player.name + "' WHERE steamid =" + player.id)
                if int(result[2]) != int(player.rating):
                    c.execute("UPDATE players SET rating =" + player.rating + " WHERE steamid =" + player.id)
            conn.commit()

        c.close()
        conn.close()