import logging
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
        data = doc.to_dict()
        return cls(
            id=doc.id,
            name=data.get('name'),
            birth_date=data.get('dateOfBirth'),
            nationality=data.get('nationality'),
            position=data.get('position')
        )
    
    @classmethod
    def is_incomplete_or_invalid(cls, request_data):
        required = {
            'id',
            'name',
            'dateOfBirth',
            'nationality',
            'position'
        }

        return not (required == set(request_data.keys()))
    
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
    
    @classmethod
    def regisatration_player(cls, player_dict):
        player_ref = db.collection(cls.COLLECTION_NAME).document()
        player_ref.set({
            'id': player_dict['id'],
            'name': player_dict['name'],
            'dateOfBirth': player_dict['dateOfBirth'],
            'nationality': player_dict['nationality'],
            'position': player_dict['position']
        })

        created_doc = player_ref.get()

        if created_doc.exists:
            player_data = created_doc.to_dict()
            player_name = player_data['name']
            logging.info(f'Document created {player_name}')
        else:
            logging.warning(f'Document with ID {player_ref.id} was not found.')

        return player_data