from app.models.planet import Planet
from flask import jsonify, abort, make_response


def error_msg(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))


def success_msg(message, status_code):
    return make_response(jsonify(dict(details=message)), status_code)


def make_planet_safely(data_dict):
    try:
        planet = Planet.from_dict(data_dict)
    except KeyError as err:
        error_msg(f"Missing key: {err}", 400)

    return planet


def replace_planet_safely(planet, data_dict):
    try:
        planet.replace_details(data_dict)
    except KeyError as err:
        error_msg(f"Missing key: {err}", 400)


def get_planet_record_by_id(id):
    try:
        id = int(id)
    except ValueError:
        error_msg(f"Invalid id: {id}", 400)

    planet = Planet.query.get(id)
    if planet:
        return planet

    error_msg(f"No planet with id: {id}", 404)
