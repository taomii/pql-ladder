from flask import Flask, jsonify, render_template
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import re

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/charly"

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Players(db.Model):
    steamid = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('steamid', 'nickname', 'rating')

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

def get_players():
    players = Players.query.all()
    result = players_schema.dump(players)
    result_sorted = sorted(result, key=lambda d: d['rating'], reverse=True)

    for i, player in enumerate(result_sorted):
        player["rank"] = i + 1

    return result_sorted

def clean_name(nick):
    return re.sub(r"[\^][0-9]","", nick)

@app.route('/', methods=['GET'])
def players():
    players = get_players()
    return {"players": players}

@app.route('/leaderboard', methods=['GET'])
def players_pretty():
    players = get_players()
    for player in players:
        player["nickname"] = clean_name(player["nickname"])
    return render_template('index.html', players = players)

@app.route('/player/<id>', methods=['GET'])
def get_player(id):
    player = Players.query.get(id)
    return player_schema.jsonify(player)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')