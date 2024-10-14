class Player:
    def __init__(self, id, name, birth_date, nationality, position):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.nationality = nationality
        self.position = position

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