from flask import Blueprint, jsonify

class Planet:
    
    def __init__(self, name, id, description, life):
        self.name = name
        self.id = id
        self.description = description
        self.life = life

planets = [
    Planet("Mercury", 1, "small, grey-silver", False),
    Planet("Venus", 2, "hot, bright", False),
    Planet("Earth", 3, "beautiful", True)
]

planet_bp = Blueprint("planets", __name__, url_prefix= "/planets")

@planet_bp.route("", methods=["GET"])

def get_all_planets():
    all_planets = []
    for planet in planets:
        all_planets.append(
            {
                "name" : planet.name,
                "id" : planet.id,
                "description" : planet.description,
                "life" : planet.life
            }
        )
    return jsonify(all_planets)
