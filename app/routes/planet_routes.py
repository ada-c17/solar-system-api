from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet import Planet
from app import db
from .planet_helpers import validate_planet



planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

#Create planet
@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.create(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.title} successfully created", 201)

#Get all planets
@planet_bp.route("", methods=["GET"])
def read_all_planets():
    title_query = request.args.get("title")
    if title_query:
        planets = Planet.query.filter_by(title=title_query)
    else:
        planets = Planet.query.all()

    planets_response = []

    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
                "moons": planet.moons
            }
        )

    return jsonify(planets_response)

'''
Created the following endpoint(s). This API can handle requests such as the following:
    - to get one existing planet, so that I can see the id, name, description, and other data of the planet.
    - such that trying to get one non-existing planet responds
    with get a 404 response, so that I know the planet resource was not found.
    - such that trying to get one planet with an invalid planet_id responds
    with get a 400 response, so that I know the planet_id was invalid.
'''

#Get one planet
@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.to_json(), 200)

#Update one planet
@planet_bp.route("/<id>", methods = ["PUT"])
def update_one_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()
    planet.update(request_body)
    db.session.commit()

    return make_response(jsonify(f"Planet # {planet.id} successfully updated"), 200)

#Delete one planet
@planet_bp.route("/<id>", methods = ["DELETE"])
def delete_one_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet # {planet.id} successfully deleted"), 200


# @planet_bp.route("/<id>/cats", methods=["POST"])
# def create_moon(id):
#     planet = validate_planet(id)

#     request_body = request.get_json()
#     new_moon = Moon.create(request_body)

#     new_moon.planet = planet
#     db.session.add(new_moon)
#     db.session.commit()

#     return make_response(jsonify(f"Moon {new_moon.name} orbiting around \
#         {new_moon.planet.title} successfully created"), 201)    


@planet_bp.route("/<id>/moons", methods=["GET"])
def read_moons(id):
    planet = validate_planet(id)

    moons_response = []
    for moon in planet.planet_moons:
        moons_response.append(moon.to_json())

    return jsonify(moons_response), 200
