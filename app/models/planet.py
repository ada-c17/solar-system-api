from app import db
from flask import abort, make_response

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    circumference = db.Column(db.Integer)
    length_of_year= db.Column(db.Integer)
    
    def to_json(self): 
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "circumference" : self.circumference,
            "length_of_year" : self.length_of_year
        }

    #update
    def update(self, request_body):
        self.name = request_body["name"]
        self.description = request_body["description"]
        self.circumference = request_body["circumference"]
        self.length_of_year = request_body["length_of_year"]

    @classmethod
    def create(cls, request_body):
        new_planet = cls(name = request_body["name"], description = request_body["description"], circumference = request_body["circumference"], length_of_year = request_body["length_of_year"])

        return new_planet
