from app import db

<<<<<<< HEAD

=======
>>>>>>> 5952d2681d2751f9f45eb2cf8657682d11f7f463
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
<<<<<<< HEAD
    has_moon = db.Column(db.Boolean, nullable=False)


    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name, 
            description = self.description,
            has_moon = self.has_moon
        )
=======
    has_moon = db.Column(db.Boolean)

    #planet turn itself into dictionary
    def to_dict(self):
        return ({
            "id": self.id,
            "name": self.name,
            "description":  self.description,
            "has_moon":  self.has_moon
        })
>>>>>>> 5952d2681d2751f9f45eb2cf8657682d11f7f463
