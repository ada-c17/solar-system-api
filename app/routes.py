from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, abort, request


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response(
            {"message": f"Planet #{planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response(
            {"message": f"Planet #{planet_id} was not found"}, 404))

    return planet


bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        has_moon=request_body["has_moon"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)


@bp.route("", methods=["GET"])
def get_planets():

    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planet_list = []
    for planet in planets:
        planet_list.append(planet.to_dict())

    return jsonify(planet_list), 200


@bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_dict()), 200

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet()
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description=request_body["description"]
    planet.has_moon=request_body["has_moon"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"), 200)

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()
    
    return make_response(jsonify(f"Planet #{planet.id} succesfully deleted"), 200)