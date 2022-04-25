from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons
    def to_json(self):
        return {
                "id": self.id,
                "name": self.name,
                "desciption": self.description,
                "moons": self.moons
            }

planets = [
            Planet(1, "Mercury", "the nearest planet to the Sun", 0),
            Planet(2, "Venus", "named after the Roman goddess of love and beauty", 0),
            Planet(3, "Earth", "Home. the only astronomical object known to harbor life", 1),
            Planet(4, "Mars", "is often called the Red Planet", 2),
            Planet(5, "Jupiter", "more then 2.5 time the mass of all other planets", 79),
            Planet(6, "Saturn", "second-largest planet in the Solar System", 82),
            Planet(7, "Uranus", "named after the Greek god of the sky", 27),
            Planet(8, "Neptune", "the densest giant planet", 14),
            Planet(9, "Pluto", "may or may not be a planet, poor Pluto", 1)
            ]
planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def read_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())
    return jsonify(planets_response), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

@planet_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json(), 200)