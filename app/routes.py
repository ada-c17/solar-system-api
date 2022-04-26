from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, distance_from_earth):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_earth = distance_from_earth

    def to_json(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "Distance from Earth": self.distance_from_earth
            }

planets = [
    Planet(1, "Mars", "Next livable planet", "131.48 million mi"),
    Planet(2, "Mercury", "Smallest planet", "94.025 million mi"),
    Planet(3, "Earth", "We live here, slowly dying", "0.0 million mi")
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def get_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "Distance from Earth": planet.distance_from_earth
            })
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"planet {planet_id} invaild"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    return abort(make_response({"message": f"planet {planet_id} does not exist"}, 404))


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json(), 200)
    
    
