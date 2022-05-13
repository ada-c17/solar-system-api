from flask import Blueprint, jsonify, abort, make_response, request
from .models.planet import Planet
from app import db

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        error_message(f"planet {planet_id} invalid", 400)

    planet = Planet.query.get(planet_id)

    if not planet:
        error_message(f"planet {planet_id} not found", 404)

    return planet

def create_planet_safely(data_dict):
    try:
        return Planet.from_dict(data_dict)
    except KeyError as err:
        error_message(f"Missing key: {err}", 400)

def replace_planet_safely(planet, data_dict):
    try:
        planet.replace_details(data_dict)
    except KeyError as err:
        error_message(f"Missing key: {err}", 400)


bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=("POST",))
def post_planet():
    request_body = request.get_json()

    new_planet = create_planet_safely(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=("GET",))
def get_planets():
    description_query = request.args.get("description")
    has_moon_query = request.args.get("has_moon")

    if description_query:
        planets = Planet.query.filter_by(description=description_query)
    elif has_moon_query:
        planets = Planet.query.filter_by(has_moon=has_moon_query)
    else:
        planets = Planet.query.all()

    result_list = [planet.to_dict() for planet in planets]

    return jsonify(result_list), 200

@bp.route("/<planet_id>", methods=("GET",))
def get_individual_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict()), 200

@bp.route("/<planet_id>", methods=("PUT",))
def put_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    replace_planet_safely(planet, request_body)

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated"), 200

@bp.route("/<planet_id>", methods=("DELETE",))
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted"), 200
