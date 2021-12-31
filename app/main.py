from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@postgresql-db:5432/charly"

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

@app.route('/', methods=['GET'])
def get_players():
    players = Players.query.all()
    result = players_schema.dump(players)
    result_sorted = sorted(result, key=lambda d: d['rating'], reverse=True)
    return {"players": result_sorted}

@app.route('/player/<id>', methods=['GET'])
def get_player(id):
    player = Players.query.get(id)
    return player_schema.jsonify(player)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')