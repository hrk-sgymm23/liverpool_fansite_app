from flask import jsonify
from services.firestore_service import db
from models.player import Player

def get_players():
    results = db.collection('players').stream()
    players = [Player.from_firestore(doc) for doc in results]
    
    players_list = [player.__dict__ for player in players]
    return jsonify(players_list), 200