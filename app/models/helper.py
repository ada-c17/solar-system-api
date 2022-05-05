from .planet import Planet
from flask import abort, make_response

def validate_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"Planet {planet_id} is not valid"}, 400))
    
    planet = Planet.query.get(planet_id)
    if not planet:
        return abort(make_response({"message": f"Planet {planet_id} does not exist"}, 404))

    return planet