from crypt import methods
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

# class Planet:
#     def __init__(self, id, name, description, length_of_day):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.length_of_day = length_of_day

#     # def to_json(self):
#     #     return {
#     #         "id": self.id,
#     #         "name": self.name,
#     #         "description": self.description,
#     #         "length_of_day": self.length_of_day
#     #     }

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

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_json())
    
    return jsonify(planets_response)
@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        length_of_day=request_body["length_of_day"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


# def valid_planet(id):
#     try:
#         id = int(id)
#     except:
#         return abort(make_response({"message": f"planet {id} is invalid"}), 400)

#     for planet in planets:
#         if planet.id == id:
#             return planet
        
#     return abort(make_response({"message": f"planet {id} not found"}),404)

# @planets_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):
#     planet = valid_planet(id)
#     return jsonify(planet.to_json())