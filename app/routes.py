from urllib import response
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort



        
    

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = []

    for planet in planets:
        planets_response.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "habitable" : planet.habitable
        })
    return jsonify(planets_response)


@planet_bp.route("", methods=["POST"])
def create_one_planet():
    request_body = request.get_json()

    new_planet = Planet(name = request_body["name"],
    description = request_body["description"],
    habitable = request_body["habitable"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.id} created")


@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):

    planet = validate_planet(id)


    return {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "habitable" : planet.habitable
        }


@planet_bp.route("/<id>", methods=["PUT"])
def update_one_planet(id):

    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.habitable = request_body["habitable"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated.")


@planet_bp.route("/<id>", methods=["DELETE"])
def delete_one_planet(id):

    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted.")




def validate_planet(planet_id):
    try:
        id = int(planet_id)
    except:
        return abort(make_response({"message" : f"planet {planet_id} is invalid."}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        return abort(make_response({"message" : f"planet {id} not found"}, 404))
    return planet


