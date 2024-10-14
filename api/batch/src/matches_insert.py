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

def insert_macthes():
    json_open = open('origin_data/files/v4_teams_64_matches.json', 'r')
    json_load = json.load(json_open)
    matches = json_load['matches']

    for match in matches:
        match_ref = db.collection('matches').document(str(match['id']))
        match_ref.set(match)

def get_all_matches():
    results = db.collection('matches').stream()
    data_list = [doc.to_dict() for doc in results]

    print(data_list)

if __name__ == '__main__':
    insert_macthes()
    print("試合情報をFirestoreに格納しました。")
    # get_all_matches()