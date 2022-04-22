from flask import Blueprint, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet:
    def __init__ (self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count

planets = [
    Planet(1, "Mercury", "red planet", 1),
    Planet(2, "Venus", "blue planet", 3),
    Planet(1, "Earth", "water planet", 1)
]

@planets_bp.route("", methods=["GET"])
def get_planets():
    planet_response_body = []
    for planet in planets:
        planet_response_body.append({
            "id": planet.id, 
            "name": planet.name,
            "description": planet.description, 
            "moon_count": planet.moon_count
            })
            
    return jsonify(planet_response_body)