from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"planet {planet_id} is invaild"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        return abort(make_response({"message": f"planet {planet_id} does not exist"}, 404))
    return planet

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        distance_from_earth=request_body['distance from earth']
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)

@planet_bp.route("", methods=["GET"])
def get_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_json() for planet in planets]

    return jsonify(planets_response, 200)

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json(), 200)

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    try:
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.distance_from_earth = request_body["distance from earth"]
        db.session.commit()
    except KeyError:
        return abort(make_response({"message": "Missing information"}, 400))

    
    return make_response(f"Planet #{planet.id} successfully updated")

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} has been deleted", 200)
<<<<<<< HEAD:app/routes.py


@planet_bp.route("/<book_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_earth = request_body["distance from earth"]
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")
=======
>>>>>>> 3242fb4274b7de0154b3854bdc9468a3ad1b0fdf:app/routes/planet_routes.py
