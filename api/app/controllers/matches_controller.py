from flask import jsonify
from models.match import Match
from datetime import datetime

def get_matches():
    matches = Match.get_all_matches()

    return jsonify(matches), 200

def get_recent_match_result():
    matches = Match.get_all_matches()
    played_matches = [match for match in matches if match['score']['winner']]
    current_date = datetime.now()

    recent_match = {
        "recent_match": min(
            played_matches,
            key=lambda match: abs(datetime.strptime(match['date'].split('T')[0], "%Y-%m-%d") - current_date) 
        )
    }

    return jsonify(recent_match), 200