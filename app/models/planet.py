from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    has_moon = db.Column(db.Boolean)

    #planet turn itself into dictionary
    def to_dict(self):
        return ({
            "id": self.id,
            "name": self.name,
            "description":  self.description,
            "has_moon":  self.has_moon
        })
