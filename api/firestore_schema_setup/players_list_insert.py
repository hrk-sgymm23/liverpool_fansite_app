# 選手データ格納ファイル
# $ python3 -m venv venv
# $ cd src/source venv/bin/activate
# $ python3 players_list_insert.py

import google.cloud.firestore
import json

db = google.cloud.firestore.Client(database='liverpool-fansite-stg')

def insert_players():
    json_open = open('./origin_data/files/v4_teams_64.json', 'r')
    json_load = json.load(json_open)
    players = json_load['squad']

    for player in players:
        player_ref = db.collection('players').document(str(player['id']))
        player_ref.set(player)

def get_all_players():
    results = db.collection('players').stream()
    data_list = [doc.to_dict() for doc in results]

    print(data_list)

if __name__ == '__main__':
    insert_players()
    get_all_players()