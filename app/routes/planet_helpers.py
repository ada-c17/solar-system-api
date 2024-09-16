from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet import Planet

def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"planet {id} is invalid"}, 400))
    planet= Planet.query.get(id)

    if not planet:
        return abort(make_response({"message": f"planet {id} is not found"}, 404))

    return planet
