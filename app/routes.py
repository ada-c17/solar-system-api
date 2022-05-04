from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.planet import Planet

solar_bp = Blueprint("planets", __name__, url_prefix="/planets")

# GET ALL and POST planet
@solar_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method== "POST":
        request_body=request.get_json()
        new_planet=Planet(
            name=request_body["name"],
            color=request_body["color"],
            description=request_body["description"])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

    elif request.method== "GET":
        name_query=request.args.get('name')
        if name_query:
            planets=Planet.query.filter_by(name=name_query)
        else:
            planets=Planet.query.all()
        planets_response=[]
        for planet in planets:
            planets_response.append(
                    {"id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "color": planet.color})
        return jsonify(planets_response), 200


# Validate if GET by Planet ID does not exist
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

# GET ONE Planet
@solar_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }

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