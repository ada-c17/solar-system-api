from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
# from .helper import validate_planet

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response(jsonify(f"planet {planet_id} invalid"), 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response(jsonify(f"planet {planet_id} not found"), 404))
    return planet

@planet_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    
    try:
        new_planet = Planet(name = request_body["name"], description = request_body["description"], moons = request_body["moons"])
        db.session.add(new_planet)
        db.session.commit()
    except:
        abort(make_response({"message":f"invalid input"}, 400))
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)
    

@planet_bp.route("", methods=["GET"])
def read_all_planets():
    

    name_query = request.args.get("name")
    moons_query = request.args.get("moons")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    elif moons_query:
        planets = Planet.query.filter_by(moons = moons_query)
    else:
        planets = Planet.query.all()
    planets_response = []    
    try:
        for planet in planets:
            planets_response.append(planet.to_json())
            
    except:
        abort(make_response(jsonify(f"planet not found"), 404))
    return make_response(jsonify(planets_response),200)




@planet_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return make_response(jsonify(planet.to_json()), 200)


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()
    try: 
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.moons = request_body["moons"]
    except:
        abort(make_response(jsonify(f"invalid data"), 400))
    
    db.session.commit()

    return jsonify(planet.to_json(), 200)

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_a_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"planet{planet_id} successfully deleted"), 200)

