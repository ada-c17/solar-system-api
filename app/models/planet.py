from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    
    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "color": self.color
                }

<<<<<<< HEAD
=======
    def update(self, req_body):
        
        self.name = req_body["name"]
        self.description = req_body["description"]
        self.color = req_body["color"]

    @classmethod
    def create(cls, req_body):
        new_planet = cls(
            name=req_body['name'],
            description=req_body['description']
            color=req_body('color']
        )

        return new_planet
>>>>>>> f3c0e71d9fdc5df838f7772e6e856f6e2fd2095d
