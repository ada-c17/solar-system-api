
from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
    

planets = [
    Planet(1, "Saturn", "Its brownish", 12),
    Planet(2, "Earth", "Its where people live", 13),   
    Planet(3, "Sun", "Its hot", 14)
]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

# GET ALL
@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        ))
    return jsonify(planets_response)