from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    length_of_day = db.Column(db.String)


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "length_of_day": self.length_of_day
        }
    @classmethod
    def create(cls, req_body):
        new_planet = cls(
            name = req_body["name"],
            description = req_body["description"],
            length_of_day = req_body["length_of_day"]
        )
        return new_planet

    def update(self, req_body):
        self.name = req_body["name"]
        self.description = req_body["description"]
        self.length_of_day = req_body["length_of_day"]