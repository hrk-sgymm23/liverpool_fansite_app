from services.firestore_service import db

class Player:
    COLLECTION_NAME = 'players'
    
    def __init__(self, id, name, birth_date, nationality, position):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.nationality = nationality
        self.position = position

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_date': self.birth_date,
            'nationality': self.nationality,
            'position': self.position
        }

    @classmethod
    def from_firestore(cls, doc):
        """FirestoreのドキュメントからPlayerオブジェクトを生成"""
        data = doc.to_dict()
        return cls(
            id=doc.id,
            name=data.get('name'),
            birth_date=data.get('dateOfBirth'),
            nationality=data.get('nationality'),
            position=data.get('position')
        )
    
    @classmethod
    def get_all_players(cls):
        results = db.collection(cls.COLLECTION_NAME).stream()
        players = [Player.from_firestore(doc) for doc in results]
    
        players_list = [player.__dict__ for player in players]

        return players_list
    
    @classmethod
    def get_player_by_name(cls, name):
        player_refs = db.collection(cls.COLLECTION_NAME) \
                    .where('name',"==", name) \
                    .get()
        player_ref = player_refs[0].to_dict()

        return player_ref
        