# 選手データ格納ファイル
# $ docker compose exec batch /bin/bash
# $ cd src/
# $ python3 players_list_insert.py

import google.cloud.firestore
import os
import json

emulator_host = os.getenv('FIRESTORE_EMULATOR_HOST')
if emulator_host:
    print(f"Connecting to Firestore emulator at {emulator_host}")
    project = os.getenv('GCLOUD_PROJECT')
    db = google.cloud.firestore.Client(project=project)
else:
    # 本番の場合は実際のDB名を指定する
    print("Connecting to Firestore production environment")
    dbname = os.environ['FIRESTORE_DB_NAME']
    db = google.cloud.firestore.Client(database=dbname)

def insert_players():
    json_open = open('origin_data/files/v4_teams_64.json', 'r')
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
    print("選手情報をFirestoreに格納しました。")
    # get_all_players()