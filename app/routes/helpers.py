from app.models.planet import Planet
from flask import make_response, abort

def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"planet {id} is invalid"}, 400))


    planet = Planet.query.get(id)
    if not planet:
        abort(make_response({"message": f"planet {id} not found"},404))
    
    return planet
