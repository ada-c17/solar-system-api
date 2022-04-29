from app import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

    def to_json(self):
        return {
                "id": self.id,
                "name": self.name,
                "desciption": self.description,
                "moons": self.moons
            }
