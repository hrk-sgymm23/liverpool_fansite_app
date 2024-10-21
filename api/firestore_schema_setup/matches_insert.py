# 選手データ格納ファイル
# $ python3 -m venv venv
# $ cd src/source venv/bin/activate
# $ python3 players_list_insert.py

import google.cloud.firestore
import json

db = google.cloud.firestore.Client(database='liverpool-fansite-stg')

def insert_macthes():
    json_open = open('./origin_data/files/v4_teams_64_matches.json', 'r')
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