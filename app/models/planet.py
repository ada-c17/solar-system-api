from app import db

'''
Defined a Planet model with the attributes id, title,
and description, and moons. Created instance method, update, to update our model. 
Class method, create, to create a new instance of planet.
'''

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    moons = db.Column(db.Boolean, nullable=False)
    planet_moons = db.relationship("Moon", back_populates="planet")


    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "moons": self.moons
        }

    def update(self, request_body):
        self.title = request_body["title"]
        self.description = request_body["description"]
        self.moons = request_body["moons"]

    @classmethod
    def create(cls,request_body):
        new_planet = cls(
            title=request_body["title"],
            description=request_body["description"],
            moons = request_body["moons"]
        )
        return new_planet
