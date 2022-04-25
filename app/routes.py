from flask import Blueprint, jsonify, abort, make_response

class Planet:
    
    def __init__(self, name, id, description, has_life=None):
        self.name = name
        self.id = id
        self.description = description
        self.has_life = has_life or False
    
    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "has_life": self.has_life
        }

planets = [
    Planet("Mercury", 1, "small, grey-silver", False),
    Planet("Venus", 2, "hot, bright", False),
    Planet("Earth", 3, "beautiful", True)
]

planet_bp = Blueprint("planets", __name__, url_prefix= "/planets")

def validate_id(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"{id} is not a valid planet id."},400))
    for planet in planets:
        if planet.id == id:
            return planet
    abort(make_response({"message": f"Planet with id of {id} was not found"},404))


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    all_planets = []
    for planet in planets:
        all_planets.append(planet.to_json())
    return jsonify(all_planets)

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    one_planet = validate_id(planet_id)

    return one_planet.to_json()