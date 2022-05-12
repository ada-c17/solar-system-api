from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .helper import validate_planet
from app.models.moon import Moon

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    
    try:
        new_planet = Planet(name = request_body["name"], description = request_body["description"])
        db.session.add(new_planet)
        db.session.commit()
    except:
        abort(make_response(jsonify({"message":f"invalid input"}), 400))
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)
    

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    

    name_query = request.args.get("name")
    # moons_query = request.args.get("moons")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    # elif moons_query:
    #     planets = Planet.query.filter_by(moons = moons_query)
    else:
        planets = Planet.query.all()
    planets_response = []    
    try:
        for planet in planets:
            planets_response.append(planet.to_json())
            
    except:
        abort(make_response(jsonify(f"planet not found"), 404))
    return make_response(jsonify(planets_response),200)




@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return make_response(planet.to_json(), 200)


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()
    try: 
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        # planet.moons = request_body["moons"]
    except:
        abort(make_response(jsonify(f"invalid data"), 400))
    
    db.session.commit()

    return jsonify(planet.to_json(), 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_a_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"planet{planet_id} successfully deleted"), 200)

@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def read_moons_for_planet(planet_id):
    planet = validate_planet(planet_id)
    moons_response = []
    for moon in planet.moons:
        moons_response.append(moon.to_json())
    return make_response(jsonify(moons_response), 200)

@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def write_moon_to_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    new_moon = Moon(name=request_body["name"], planet=planet)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} of the planet {new_moon.planet.name} successfully created"), 201)