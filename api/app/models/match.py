from services.firestore_service import db

class Match:
    COLLECTION_NAME = 'matches'

    def __init__(self, id, away_team, home_team, score, date):
        self.id = id
        self.away_team = away_team
        self.home_team = home_team
        self.score = score
        self.date = date

    @classmethod
    def from_firestore(cls, doc):
        data = doc.to_dict()
        return cls(
            id=doc.id,
            away_team=data.get('awayTeam'),
            home_team=data.get('homeTeam'),
            score=data.get('score'),
            date=data.get('utcDate')
        )

    @classmethod
    def get_all_matches(cls):
        results = db.collection(cls.COLLECTION_NAME).stream()
        matches = [Match.from_firestore(doc) for doc in results]
        
        matches_list = [match.__dict__ for match in matches]

        return matches_list
        