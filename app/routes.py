from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.planet import Planet
from .helper import validate_planet

solar_bp = Blueprint("planets", __name__, url_prefix="/planets")

# GET and POST planets
@solar_bp.route("", methods=["POST", "GET"])
def handle_planets():
    # Create a planet
    if request.method== "POST":
        request_body=request.get_json()
        new_planet=Planet.create(request_body)
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

    # Get all planets, or filter by planet name
    elif request.method== "GET":
        name_query=request.args.get('name')
        if name_query:
            planets=Planet.query.filter_by(name=name_query)
        else:
            planets=Planet.query.all()
        planets_response=[]
        for planet in planets:
            planets_response.append(planet.to_json())

        return jsonify(planets_response), 200


# GET ONE Planet
@solar_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json()), 200

# UPDATE Planet
@solar_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.update(request_body)

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

# DELETE Planet
@solar_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")