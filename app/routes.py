from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix= "/planets")

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    all_planets = []
    if len(request.args) != 0:
        planets = Planet.query.filter_by(**request.args)
    else:
        planets = Planet.query.all()

    for planet in planets:
        all_planets.append(planet.to_json())

    return jsonify(all_planets)

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    one_planet = Planet.validate_id(planet_id)

    return one_planet.to_json()

@planet_bp.route("", methods=["POST"])
def create_planet():
    planet_data = request.get_json()
    new_planet = Planet(
        name=planet_data['name'],
        description=planet_data['description'],
        has_life=planet_data['has_life']
        )
    
    db.session.add(new_planet)
    db.session.commit()

    return jsonify(f"Planet {new_planet.name} successfully created"), 201

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = Planet.validate_id(planet_id)

    new_data = request.get_json()

    planet.name = new_data['name']
    planet.description = new_data['description']
    planet.has_life = new_data['has_life']

    db.session.commit()

    return jsonify(f"Planet {planet.name} successfully updated"), 200

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.validate_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return jsonify(f"Planet {planet.name} successfully deleted"), 200