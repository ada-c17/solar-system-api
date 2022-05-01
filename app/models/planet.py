from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
<<<<<<< HEAD
    description = db.Column(db.String)
    color = db.Column(db.String)
    
    def to_json(self):
        return {"ID": self.id,
                "Name": self.name,
                "Description": self.description,
                "Color": self.color
                }
=======
    color = db.Column(db.String)
    description=db.Column(db.String)
>>>>>>> d5b0ed65df6c5d7d8c660d713c4c1da999dc4699
