from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
# class Planet:
#     def __init__(self, id, name, moons, description):
#         self.id = id
#         self.name = name
#         self.moons = moons
#         self.description = description 


# planets = [
#     Planet(1, "Mercury", 0, "The first planet."),
#     Planet(2, "Venus", 0, "The second planet."),
#     Planet(3, "Earth", 1, "The third planet.")

# ]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        id=request_body["id"],
        name=request_body["name"],
        moons=request_body["moons"],
        description=request_body["description"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
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

@planets_bp.route("/<planet_id>", methods=['PUT'])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.moons = request_body["moons"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("<planet_id>", methods=['DELETE'])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Book #{planet.id} successfully deleted")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    
    return planet
    


    