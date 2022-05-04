from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
from .helpers import validate_planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def post_new_planet():
    request_body = request.get_json()
    
    new_planet = Planet.create_planet(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_json() for planet in planets]
        
    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json()), 200


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    update_body = request.get_json()
    planet = validate_planet(planet_id)

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted", 200)
