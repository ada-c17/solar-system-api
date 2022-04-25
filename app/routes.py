from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color 

    def to_dict(self):
        return dict(
        id=self.id,
        name=self.name,
        description=self.description,
        color=self.color,
        )

planets = [
    Planet(1, "Mercury", "Super small, comparatively", "slate gray"),
    Planet(2, "Venus", "It's sooo hot!", "yellow-white"),
    Planet(3, "Earth", "Home to humans", "blue-green"),
    Planet(4, "Mars", "The red one", "red"),
    Planet(5, "Jupiter", "The biggest of them all", "orange-yellow"),
    Planet(6, "Saturn", "What beautiful rings it has!", "hazy yellow-brown"),
    Planet(7, "Uranus", "Tilted sideways", "blue-green"),
    Planet(8, "Neptune", "Giant, stormy, blue", "blue"),
    Planet(9, "Maybe Pluto", "Is it really a planet??", "reddish-brown")
    ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({"message":f"invalid id: {id}"}, 400))

    for planet in planets:
        if planet.id == id:
            return planet

    abort(make_response({"Message":f"Planet ID {id} not found"}, 404))

@bp.route("", methods=["GET"])
def get_planets():
    results_list = []
    for planet in planets:
        results_list.append(planet.to_dict())
    return jsonify(results_list)

@bp.route("/<id>", methods=["GET"])
def get_planet(id):
    planet = validate_planet(id)
    return planet.to_dict(), 200
