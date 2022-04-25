from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, distance_from_earth):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_earth = distance_from_earth


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
