from app import db
from app.models.planet import Planet
from app.models.moon import Moon
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

@planet_bp.route("/<planet_id>/moons", methods=['POST'])
def add_moons(planet_id):
    planet = Planet.validate_id(planet_id)
    moon_data = request.get_json()
    new_moon = Moon(
        size = moon_data['size'], 
        description = moon_data['description'],
        had_life = moon_data['had_life']
        )
    planet.moons.append(new_moon)
    db.session.commit()

    return jsonify({"New moon successfully added."}), 201

@planet_bp.route("/<planet_id>/moons", methods=['GET'])
def get_moons(planet_id):
    planet = Planet.validate_id(planet_id)

    moons = [moon.to_json() for moon in planet.moons]

    return jsonify(moons), 200
