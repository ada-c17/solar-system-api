from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .helpers import validate_planet

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.create(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} has been created"), 201)

@ planet_bp.route("", methods=["GET"])
def get_planets():
    planet_query = request.args.get("name")
    color_query = request.args.get("color")
    if planet_query:
        planets = Planet.query.filter_by(name=planet_query)
    elif color_query:
        planets = Planet.query.filter_by(color=color_query)
    else:
        planets = Planet.query.all()

    planets_response = [planet.to_json() for planet in planets]

    return make_response(jsonify(planets_response), 200)

@ planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return make_response(jsonify(planet.to_json()), 200)

@ planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    try:
        Planet.update(request_body)
        db.session.commit()
    except KeyError:
        return abort(make_response(jsonify("Missing information")), 400)

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"), 200)

@ planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet.id} has been deleted"), 200)
