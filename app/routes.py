from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    try:
        planet = Planet.from_dict(request_body)
    
    except KeyError as err:
        abort(make_response(jsonify(details=f"Missing key: {err} invalid"), 400))

    db.session.add(planet)
    db.session.commit()

    # return make_response(jsonify(f"Planet {planet.name} successfully created"), 201)
    return jsonify(planet.to_dict()), 201

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")

    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

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