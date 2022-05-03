from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
    
    # def to_json(self):
    #     return {
    #         "id": self.id, 
    #         "name": self.name,
    #         "description": self.description, 
    #         "moon_count": self.moon_count
    #     }

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Planet {id} is not valid"}, 400))
    planet = Planet.query.get(id)
    if not planet:
        abort(make_response({"message": f"Planet {id} not found"}, 404))
    return planet

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moon_count=request_body["moon_count"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_planets():
    planets = Planet.query.all()
    planet_response_body = []
    for planet in planets:
        planet_response_body.append(planet.to_json())
            
    return jsonify(planet_response_body), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.to_json())

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_count = request_body["moon_count"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")