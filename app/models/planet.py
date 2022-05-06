from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    moons = db.Column(db.Integer)
    description = db.Column(db.String)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            moons=self.moons,
            description=self.description
        )

@classmethod    
def from_dict(cls, data_dict):
    return cls(
        name=data_dict["name"],
        moons=data_dict["moons"],
        description=data_dict["description"])
    