from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
from .helpers import validate_planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# Get all planets
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    id_query = request.args.get("id")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    elif id_query:
        planets = Planet.query.filter_by(id = id_query)
    else:
        planets = Planet.query.all() 

    planets_response = []
    # planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_json())
    
    return jsonify(planets_response),200

# Get one planet
@planets_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.to_json()),200

# Create planets
@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = Planet.create(request_body)
    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)
    # return make_response(f"Planet {new_planet.name} successfully created", 201)
# Update one planet
@planets_bp.route("/<id>", methods=["PUT"])
def update_one_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()
    planet.update(request_body)
    db.session.commit()
    
    return make_response(f"Planet {id} successfully updated", 200)

# Delete one planet
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_one_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet {id} successfully deleted", 200)



        
# planets =  [
#     Planet(1, "Mercury", "The closest planet to the Sun, and the smallest planet in our solar system", "58d 15h 30m"),
#     Planet(2, "Venus", "The second planet from the Sun and Earth's closest planetary neighbor", "116d 18h 0m"),
#     Planet(3, "Mars", "The fourth planet from the Sun and the second-smallest planet in the Solar System", "1d 0h 37m"),
#     Planet(4, "Jupiter", "The fifth planet from the Sun and the largest in the Solar System", "0d 9h 56m"),
#     Planet(5, "Saturn", "The sixth planet from the Sun and the second-largest in the Solar System, after Jupiter", "0d 10h 42m"),
#     Planet(6, "Uranus", "The third-largest planetary radius and fourth-largest planetary mass in the Solar System", "0d 17h 14m"),
#     Planet(7, "Neptune", "The eighth and farthest-known Solar planet from the Sun", "0d 16h 6m"),
#     Planet(8, "Pluto", "A dwarf planet in the Kuiper belt, after Pluto was discovered in 1930, it was declared the ninth planet from the Sun", "6d 9h 36m")
#     ]        
