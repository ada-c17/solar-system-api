from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)

    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "color": self.color
                }
    def update_planet(self,request_body):
        self.name = request_body["name"]
        self.description =request_body["description"]
        self.color= request_body["color"]
    
    @classmethod
    def create_planet(cls, request_body):
        new_planet = cls(name = request_body["name"],
                        description = request_body["description"], 
                        color = request_body["color"])
        return new_planet