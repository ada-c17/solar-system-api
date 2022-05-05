from app.models.planet import Planet
from .routes_helper import error_msg

def make_planet_safely(data_dict):
    try:
        planet = Planet.from_dict(data_dict)
    except KeyError as err:
        error_msg(f"Missing key: {err}", 400)

    return planet


def replace_planet_safely(planet, data_dict):
    try:
        planet.replace_details(data_dict)
    except KeyError as err:
        error_msg(f"Missing key: {err}", 400)


def get_planet_record_by_id(id):
    try:
        id = int(id)
    except ValueError:
        error_msg(f"Invalid id: {id}", 400)

    planet = Planet.query.get(id)
    if planet:
        return planet

    error_msg(f"No planet with id: {id}", 404)