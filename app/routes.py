from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


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
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response, 200)


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"planet {planet_id} is invaild"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        return abort(make_response({"message": f"planet {planet_id} does not exist"}, 404))
    return planet


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json(), 200)


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} has been deleted", 200)


@planet_bp.route("/<book_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_earth = request_body["distance from earth"]
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")
