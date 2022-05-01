from flask import Blueprint, jsonify, abort, make_response


# class Planet:
#     def __init__(self, name, id, description, color):
#         self.name = name
#         self.id = id
#         self.description = description
#         self.color = color
    
#     def to_json(self):
#         return {"Name": self.name,
#                 "ID": self.id,
#                 "Description": self.description,
#                 "Color": self.color
#                 }

# planets = [
#     Planet("Earth", 3, "Earth is the 3rd planet in solar system", "blue"),
#     Planet("Mars", 4, "Mars is the 4th planet in solar system", "red"),
#     Planet("Jupiter", 5, "Jupiter is the 5th planet in solar system", "tan")
# ]

def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"planet {id} is invalid"}, 400))
    for planet in planets :
        if planet.id == id:
            return jsonify(planet.to_json()), 200
    return abort(make_response({"message": f"planet {id} is not found"}, 404))
# first string is flask blueprint name
# run in localhost need to add/planets at the end
solar_bp = Blueprint("", __name__, url_prefix="/planets")


@solar_bp.route("", methods=["GET"])
def see_planets():
    all_planets = []
    for planet in planets:
        all_planets.append(
          planet.to_json()
        )
    return jsonify(all_planets), 200

#Get one planet
@solar_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet_response = validate_planet(id)
    return planet_response








