# Helper function:
from flask import abort, make_response, jsonify
from app.models.planet import Planet

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response(jsonify(f"planet {planet_id} invalid"), 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response(jsonify(f"planet {planet_id} not found"), 404))
    return planet