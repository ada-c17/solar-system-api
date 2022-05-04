from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# planets = [
#     Planet(1, "Arrakis", "A desert planet, source of Spice.", True),
#     Planet(2, "Bela Tegeuse", "The fifth planet of Keuntsing.", False),
#     Planet(3, "Tupile", "Sanctuary planet for defeated houses of the Imperium.", True),
#     Planet(4, "Ix", "Supreme machine culture.", False)
# ]

planets_bp = Blueprint("Planets", __name__, url_prefix="/planets")

# Helper Functions:

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

def success_message(message, status_code=200):
    return make_response(jsonify(dict(details=message)), status_code)

def return_database_info(return_value):
    return make_response(jsonify(return_value))

def get_planet_record_by_id(id):
    try:
        id = int(id)
    except ValueError:
        error_message(f"Invalid id: {id}", 400)
    planet = Planet.query.get(id)
    if planet:
        return planet
    else:
        error_message(f"Planet id: {id} not found", 404)

def discover_planet_safely(data_dict):
    try:
        return Planet.create_from_dict(data_dict)
    except KeyError as err:
        error_message(f"Missing key: {err}", 400)


def update_planet_safely(planet, data_dict):
    try:
        planet.update_self(data_dict)
    except ValueError as err:
        error_message(f"Invalid key: {err}. Planet not updated.", 400)
    except KeyError as err:
        error_message(f"Missing key: {err}. Planet not updated.", 400)




# Route Functions:

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    moon_param = request.args.get("has_moons")

    if moon_param:
        planets = Planet.query.filter_by(has_moons=moon_param)
    else:
        planets = Planet.query.all()
    
    all_planets = [
        planet.self_to_dict()
        for planet in planets
    ]
    return return_database_info(all_planets)


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = get_planet_record_by_id(planet_id)
    return return_database_info(planet.self_to_dict())


@planets_bp.route("", methods=["POST"])
def discover_planet():
    request_body = request.get_json()
    new_planet = Planet.create_from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return success_message(f"Planet {new_planet.name} successfully added to the Planets Database.", 201)


@planets_bp.route("/<planet_id>", methods=["PUT", "PATCH"])
def update_planet_by_id(planet_id):
    planet = get_planet_record_by_id(planet_id)

    request_body = request.get_json()
    update_planet_safely(planet, request_body)

    db.session.commit()

    return return_database_info(planet.self_to_dict())


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_record_by_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return success_message(f"Planet {planet.name} successfully deleted from the Planets Database.")