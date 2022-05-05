from app import db
from app.models.planet import Planet
from .routes_helper import success_msg
from .planet_routes_helper import make_planet_safely, replace_planet_safely, get_planet_record_by_id
from flask import Blueprint, jsonify, make_response, abort, request


bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = make_planet_safely(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return jsonify(new_planet.to_dict()), 201


@bp.route("", methods=["GET"])
def get_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planet_list = [planet.to_dict() for planet in planets]

    return jsonify(planet_list), 200


@bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = get_planet_record_by_id(planet_id)
    return jsonify(planet.to_dict()), 200


@bp.route("/<planet_id>", methods=["PUT"])
def replace_planet(planet_id):
    request_body = request.get_json()
    planet = get_planet_record_by_id(planet_id)

    replace_planet_safely(planet, request_body)

    db.session.commit()

    return success_msg(f"Planet #{planet.id} successfully updated", 200)


@bp.route("/<planet_id>", methods=["PATCH"])
def update_planet_with_id(planet_id):
    planet = get_planet_record_by_id(planet_id)
    request_body = request.get_json()

    planet.check_keys(request_body)

    db.session.commit()

    return success_msg(f"Planet #{planet.id} successfully updated", 200)


@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_record_by_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return success_msg(f"Planet #{planet.id} successfully deleted", 200)
