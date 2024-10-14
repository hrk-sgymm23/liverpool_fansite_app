import base64
import os
from flask import Flask, request
import google.cloud.firestore
import json


app = Flask(__name__)
emulator_host = os.getenv('FIRESTORE_EMULATOR_HOST')

API_V1_PATH = "/api/v1"

print(f"{emulator_host=}")
if emulator_host:
    print(f"Connecting to Firestore emulator at {emulator_host}")
    project = os.getenv('GCLOUD_PROJECT')
    db = google.cloud.firestore.Client(project=project)
else:
    # 本番の場合は実際のDB名を指定する
    print("Connecting to Firestore production environment")
    dbname = os.environ['FIRESTORE_DB_NAME']
    db = google.cloud.firestore.Client(database=dbname)


@app.route(f"{API_V1_PATH}/players", methods=["GET"])
def get_players():
    results = db.collection('players').stream()
    print(f"result: {results}")
    players = [doc.to_dict() for doc in results]

    players_dict = {}
    players_dict = players
    json.dumps(players_dict)

    return (players_dict, 200)

@app.route(f"{API_V1_PATH}/matches", methods=["GET"])
def get_matches():
    results = db.collection('matches').stream()
    print(f"result: {results}")
    matches = [doc.to_dict() for doc in results]

    matches_dict = {}
    matches_dict = matches
    json.dumps(matches_dict)

    return (matches_dict, 200)