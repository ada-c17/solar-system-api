from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_count = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id, 
            "name": self.name,
            "description": self.description, 
            "moon_count": self.moon_count
        }

    def update(self, req_body):
        self.name = req_body["name"]
        self.description = req_body["description"]
        self.moon_count = req_body["moon_count"]

    @classmethod
    def create(cls, req_body):
        new_planet = cls(
                    name=req_body["name"],
                    description=req_body["description"],
                    moon_count=req_body["moon_count"]
                    )
        return new_planet