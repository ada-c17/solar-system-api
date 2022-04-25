from os import abort
from flask import Blueprint, jsonify, make_response, abort


class Planet:

    def __init__(self, id, name, description, habitable):
        self.id = id
        self.name = name
        self.description = description
        self.habitable = habitable

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "habitable": self.habitable
        }
        
    
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
        planets_response.append(
            planet.to_json()
        )
    return jsonify(planets_response)


def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message" : f"planet {id} is invalid."}, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet
    return abort(make_response({"message" : f"planet {id} not found"}, 404))

@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_json())

