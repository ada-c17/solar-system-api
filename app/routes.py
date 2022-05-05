from app import db
from .models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

#helper function to get one planet by id or return error message
def get_planet_by_id(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify(dict(details=f"Invalid id {id}")), 400))

    planet = Planet.query.get(id)

    if planet:
        return planet
    else:
        abort(make_response(jsonify(dict(details=f"Invalid planet {id}")), 404))

    
#create a planet
@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        has_moon=request_body["has_moon"],
    )
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created"), 201

#read all planets
@bp.route("", methods=["GET"])
def read_all_planets():
    #query params for /planets endpoint
    #planets?<key>=<value>
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    has_moon_query = request.args.get("has_moon")


    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif description_query:
        planets = Planet.query.filter_by(description=description_query)
    elif has_moon_query:
        planets = Planet.query.filter_by(has_moon=has_moon_query)
    else:
        planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)

#get one existing planet   
@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = get_planet_by_id(planet_id)
    return jsonify(planet.to_dict())

#replace one existing planet
@bp.route("/<planet_id>", methods=["PUT"])
def replace_one_planet_by_id(planet_id):
    request_body = request.get_json()
    planet = get_planet_by_id(planet_id)

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_moon = request_body["has_moon"]

    db.session.commit()
    return make_response(f"Planet {planet.id} successfully added"), 200

#update part of one existing planet
@bp.route("<planet_id>", methods=["PATCH"])
def update_planet_by_id(planet_id):
    request_body = request.get_json()
    planet = get_planet_by_id(planet_id)

    planet_keys = request_body.keys()

    if "name" in planet_keys:
        planet.name = request_body["name"]
    if "description" in planet_keys:
        planet.description = request_body["description"]
    if "has_moon" in planet_keys:
        planet.has_moon = request_body["has_moon"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated"), 200

#delete record of planet
@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet_by_id(planet_id):
    planet = get_planet_by_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted"), 200











    
