from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, moons, description):
        self.id = id
        self.name = name
        self.moons = moons
        self.description = description 


planets = [
    Planet(1, "Mercury", None, "The first planet."),
    Planet(2, "Venus", None, "The second planet."),
    Planet(3, "Earth", 1, "The third planet.")

]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "moons": planet.moons,
            "description": planet.description
        })
    return jsonify(planets_response)