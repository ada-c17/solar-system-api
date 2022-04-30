from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, has_moon=None):
        self.id = id
        self.name = name
        self.description = description
        self.has_moon = has_moon

planets = [
    Planet(1, "Mercury", "terrestrial", False),
    Planet(2, "Venus", "terrestrial", False),
    Planet(3, "Earth", "terrestrial", True),
    Planet(4, "Mars", "terrestrial", True)
]

bp = Blueprint("planets", __name__, url_prefix="/planets")


@bp.route("", methods=("GET",))
def get_planets():
    list_of_planets = []
    for planet in planets:
        list_of_planets.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_moon": planet.has_moon
        })
    return jsonify(list_of_planets), 200
