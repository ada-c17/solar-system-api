from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    moons = db.relationship("Moon", back_populates="planet")
    
    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "color": self.color
                }

    def update(self, req_body):
        
        self.name = req_body["name"]
        self.description = req_body["description"]
        self.color = req_body["color"]

    @classmethod
    def create(cls, req_body):
        new_planet = cls(
            name=req_body['name'],
            description=req_body['description'],
            color=req_body['color']
        )

        return new_planet
