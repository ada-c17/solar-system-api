# from app import db
# from flask import abort, make_response, jsonify

# class Planet(db.Model):
    
#     name = db.Column(db.String)
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     description = db.Column(db.String)
#     has_life = db.Column(db.Boolean)
    
#     def to_json(self):
#         return {
#             "name": self.name,
#             "id": self.id,
#             "description": self.description,
#             "has_life": self.has_life
#         }
    
#     @classmethod
#     def validate_id(cls, planet_id):
#         try:
#             planet_id = int(planet_id)
#         except:
#             abort(make_response(jsonify(f"{planet_id} is not a valid planet id."),400))
#         planet = cls.query.get(planet_id)  
#         if planet:
#             return planet
#         abort(make_response(jsonify(f"Planet with id of {planet_id} was not found"),404))

from app import db

class Moon(db.Model):
    moon_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Integer)
    description = db.Column(db.String)
    had_life = db.Column(db.Boolean)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', back_populates='moons')
