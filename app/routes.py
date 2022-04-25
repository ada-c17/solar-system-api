from flask import Blueprint, jsonify, make_response, abort

class Planet:
    def __init__(self, id, name, description, has_moon=None):
        self.id = id
        self.name = name
        self.description = description
        self.has_moon = has_moon

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            has_moon = self.has_moon,
        )

planets = [
    Planet(1, "Mercury", "terrestrial", False),
    Planet(2, "Jupiter", "gaseous", True),
    Planet(3, "Earth", "terrestrial", True)
]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    abort(make_response({"message": f"planet {planet_id} was not found"}, 404))

bp = Blueprint("planets_bp",__name__, url_prefix="/planets")

@bp.route("", methods=("GET",))
def list_planets():
    planet_list = [planet.to_dict() for planet in planets]

    return jsonify(planet_list)

@bp.route("/<planet_id>", methods=("GET",))
def get_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict())