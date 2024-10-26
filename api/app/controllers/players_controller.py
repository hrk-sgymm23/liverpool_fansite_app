from flask import jsonify, request
from models.player import Player

def get_players():
    players = Player.get_all_players()
    players_dict = {
        'players': players
    }

    return jsonify(players_dict), 200

def get_player():
    name = request.args.get('name')

    if name is None:
        return jsonify({"error": "name is required"}), 400

    player = Player.get_player_by_name(name)

    return jsonify(player), 200

def create_player():
    data = request.get_json()
    player = Player.regisatration_player(data)

    return jsonify(player), 200
