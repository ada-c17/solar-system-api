from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request


# planets = [
#     Planet(1, "Mars", "Next livable planet", "131.48 million mi"),
#     Planet(2, "Mercury", "Smallest planet", "94.025 million mi"),
#     Planet(3, "Earth", "We live here, slowly dying", "0.0 million mi")
# ]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        distance_from_earth=request_body['Distance from Earth']
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)


# @planet_bp.route("", methods=["GET"])
# def get_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "Distance from Earth": planet.distance_from_earth
#             })
#     return jsonify(planets_response)

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         return abort(make_response({"message": f"planet {planet_id} is invaild"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     return abort(make_response({"message": f"planet {planet_id} does not exist"}, 404))


# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return jsonify(planet.to_json(), 200)
