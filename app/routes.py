from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        color = request_body["color"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} successfully created", 201

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }
        )
    return jsonify(planets_response)

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = Planet.query.get(planet_id)
    return planet.to_dict()