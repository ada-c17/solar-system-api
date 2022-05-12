from flask import Blueprint, jsonify, abort, make_response, request
from .models.planet import Planet
from app import db

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))


bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=("POST",))
def post_planets():
    request_body = request.get_json()

    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        has_moon=request_body["has_moon"],)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=("GET",))
def get_planets():
    planets = Planet.query.all()

    result_list = [planet.to_dict() for planet in planets]

    return jsonify(result_list), 200

# @bp.route("/<planet_id>", methods=("GET",))
# def get_individual_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "has_moon": planet.has_moon
#             }, 200
