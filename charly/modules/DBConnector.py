import sqlite3

class DBConnector:

    def write(self, playerList):

        conn = sqlite3.connect('ranking.db')
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
