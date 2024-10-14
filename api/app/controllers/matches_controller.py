from flask import jsonify
from services.firestore_service import db
from models.match import Match
from datetime import datetime

def prepare_matches():
    results = db.collection('matches').stream()
    matches = [Match.from_firestore(doc) for doc in results]
    
    matches_list = [match.__dict__ for match in matches]

    return matches_list

def get_matches():
    matches = prepare_matches()

    return jsonify(matches), 200

# wip
def get_recent_match_result():
    matches = prepare_matches()
    print(matches)

    current_date = datetime.now()

    recent_match = min(
        matches,
        key=lambda match: abs(datetime.strptime(match['date'], "%Y-%m-%d") - current_date) 
    )

    return jsonify(recent_match), 200