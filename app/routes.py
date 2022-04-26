from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, moons, description):
        self.id = id
        self.name = name
        self.moons = moons
        self.description = description 


planets = [
    Planet(1, "Mercury", 0, "The first planet."),
    Planet(2, "Venus", 0, "The second planet."),
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

@planets_bp.route("<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "moons": planet.moons,
        "description": planet.description 
        } 

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))