import re
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.Planet import Planet

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

#Validate planet data
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"Planet {planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)
    
    if not planet:       
        return abort(make_response({"message": f"Planet {planet_id} is not found"}, 404))
    return planet

#GET all planets or GET by NAME query
@planet_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name").title()
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planet_response = []
    for planet in planets:
        planet_response.append({
            "id" : planet.planet_id,
            "name" : planet.name,
            "description" : planet.description,
            "color" : planet.color
        })
    if not planet_response:
        return abort(make_response({"message": f"Planet {name_query} is not found"}, 404))
    
    return jsonify(planet_response)

#POST new planet
@planet_bp.route("", methods=["POST"])
def add_new_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        color=request_body["color"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} was successfully created", 201)


#GET one planet by id
@planet_bp.route("<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
            "id" : planet.planet_id,
            "name" : planet.name,
            "description" : planet.description,
            "color" : planet.color
        }


#UPDATE one planet by id with PUT
@planet_bp.route("<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet #{planet.planet_id}, '{planet.name}', successfully updated.")


#DELETE one planet by id
@planet_bp.route("<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)
   
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.planet_id}, '{planet.name}', successfully deleted.")