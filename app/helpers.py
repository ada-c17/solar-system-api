from flask import abort, make_response
from .models.planet import Planet

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Planet {id} is not valid"}, 400))

    planet = Planet.query.get(id)

    if not planet:
        abort(make_response({"message": f"Planet {id} not found"}, 404))
        
    return planet