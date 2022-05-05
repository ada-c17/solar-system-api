from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app.models.helper import validate_id

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planet_response = []
    planets = Planet.query.all()
    for planet in planets:
        planet_response.append(planet.to_json())

    return jsonify(planet_response), 200

@planets_bp.route("", methods = ["POST"])
def make_new_planet():
    request_body = request.get_json()
    new_planet = Planet.create_planet(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"planet {new_planet.id} successfully created"), 201)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_id(planet_id)
    return jsonify(planet.to_json()), 200

@planets_bp.route("/<planet_id>", methods = ["PUT"])
def update_one_planet(planet_id):
    planet = validate_id(planet_id)
    request_body = request.get_json()

    planet.update_planet(request_body)

    db.session.commit()
    return make_response(f"Planet {planet_id} successfully updated"), 200

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_id(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet {planet_id} successfully deleted"), 200
    
    

