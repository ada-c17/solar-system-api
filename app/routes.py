import re
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from .models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, has_moon=None):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.has_moon = has_moon

#     def to_json(self):
#         return dict(
#         id = self.id,
#         name = self.name, 
#         description = self.description,
#         has_moon = self.has_moon
            # )
# planets = [
#     Planet(1, "Mercury", "terrestrial", False),
#     Planet(2, "Jupiter", "gaseous", True),
#     Planet(3, "Earth", "terrestrial", True)
# ]

#instantiate blueprint object
bp = Blueprint("planets_bp",__name__, url_prefix="/planets")

#design endpoint with blueprint tag
"""..to get all existing planets, so that I can see a list of planets,
with their id, name, description, and other data of the planet."""

@bp.route("", methods=["GET"])
def read_all_planets():
    # if request.method == "GET":
    #     planets = Planet.query.all()
        planets_response = []
        name_query = request.args.get("name")

        if name_query is not None:
            planets = Planet.query.filter_by
            name = name_query
        else:
            planets = Planet.query.all()

        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "has_moon": planet.has_moon
            })
        return jsonify(planets_response)


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    has_moon=request_body["has_moon"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

def get_planet_by_id(id):
    try:
        id = int(id)
    except ValueError: 
        abort(make_response(jsonify(dict(details=f"Invalid id {id}")), 400))

    planet = Planet.query.get(id)

    if planet:
        return planet 

    else: 
        abort(make_response(jsonify(dict(details=f"Invalid id {id}")), 404))

@bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = get_planet_by_id(planet_id)
    return jsonify(planet.to_dict())

@bp.route("/<planet_id>", methods=["PUT"])
def replace_planet(planet_id):
    planet = get_planet_by_id(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_moon = request_body["has_moon"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated"), 200


# FLASK_ENV=developer flask run

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = get_planet_by_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

    
