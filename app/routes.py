from flask import Blueprint, jsonify, abort, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet:
    def __init__ (self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count
    
    def to_json(self):
        return {
            "id": self.id, 
            "name": self.name,
            "description": self.description, 
            "moon_count": self.moon_count
        }

planets = [
    Planet(1, "Mercury", "red planet", 1),
    Planet(2, "Venus", "blue planet", 3),
    Planet(1, "Earth", "water planet", 1)
]

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Planet {id} is not valid"}, 400))

    for planet in planets:
        if planet.id == id:
            return planet
    
    return abort(make_response({"message": f"Planet {id} not found"}, 404))

@planets_bp.route("", methods=["GET"])
def get_planets():
    planet_response_body = []
    for planet in planets:
        planet_response_body.append(planet.to_json())
            
    return jsonify(planet_response_body)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_json())