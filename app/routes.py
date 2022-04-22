from flask import Blueprint, jsonify

class Planet:

    def __init__(self, id, name, description, habitable):
        self.id = id
        self.name = name
        self.description = description
        self.habitable = habitable
    
planets = [
    Planet(1, "Mercury", "Small, hot, first planet", False),
    Planet(2, "Venus", "Medium, bright, second planet", False),
    Planet(3, "Earth", "Medium, Oceans, third planet", True)
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "habitable": planet.habitable,
        }
        )
    return jsonify(planets_response)
