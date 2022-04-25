from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, has_moon=None):
        self.id = id
        self.name = name
        self.description = description
        self.has_moon = has_moon

    def to_json(self):
        return dict(
        id = self.id,
        name = self.name, 
        description = self.description,
        has_moon = self.has_moon
            )


planets = [
    Planet(1, "Mercury", "terrestrial", False),
    Planet(2, "Jupiter", "gaseous", True),
    Planet(3, "Earth", "terrestrial", True)
]

#instantiate blueprint object
bp = Blueprint("planets_bp",__name__, url_prefix="/planets")

#design endpoint with blueprint tag
"""..to get all existing planets, so that I can see a list of planets,
with their id, name, description, and other data of the planet."""

# @bp.route("", methods=["GET"])
# def list_planets():
#     list_of_planets = [dict(
#         id = planet.id,
#         name = planet.name,
#         description = planet.description,
#         has_moon = planet.has_moon,  
#     ) for planet in planets]

#     return jsonify(list_of_planets)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

@bp.route("", methods=["GET"])
def handle_planets():
    planet_response = [planet.to_json() for planet in planets]

    return jsonify(planet_response)

@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json())


# FLASK_ENV=developer flask run

    
