from flask import Blueprint, jsonify, make_response, abort, request
from app.models.planet import Planet
from app import db

'''
Defined a Planet class with the attributes id, name,
and description, and moons. Also, Created a list of Planet instances.
'''

# class Planet():
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons

#     def to_json(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "moons": self.moons
#         }

# planets = [
#     Planet(1, "Mercury", ["Grey", "closest to the sun", "smallest planet"], False),
#     Planet(2, "Venus", ["Brown and grey", "hottest planet"], False),
#     Planet(3, "Earth", ["Blue, brown green and white", "water world","1 moon"], True),
#     Planet(4, "Mars", ["Red, brown and tan", "2 moons"], True),
#     Planet(5, "Jupiter", ["Brown, orange and tan, with white cloud stripes","largest planet", "79 moons"], True),
#     Planet(6, "Saturn", ["Golden, brown, and blue-grey"," large and distinct ring system" ,"82 moons"], True),
#     Planet(7, "Uranus", ["Blue-green", " holds the record for the coldest temperature ever measured in the solar system ","27 moons"], True),
#     Planet(8, "Neptune", ["Blue"," on average the coldest planet" ,"14 moons"], True)
# ]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

#CREATE PLANET

# Create planet
@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(title=request_body["title"],
                    description=request_body["description"],
                    moons = request_body["moons"]
                    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.title} successfully created", 201)

#Get all planets
@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    #make_response.append(planet.to_json())

    for planet in planets:
        #planets_response.append(planet.to_json()) 
        planets_response.append(
            {
                "id": planet.id,
                "title": planet.title,
                "description": planet.description,
                "moons": planet.moons
            }
        )

    return jsonify(planets_response)

'''
Created the following endpoint(s). This API can handle requests such as the following:
...to get one existing planet, so that I can see the id, name, description,
and other data of the planet.
... such that trying to get one non-existing planet responds
with get a 404 response, so that I know the planet resource was not found.
... such that trying to get one planet with an invalid planet_id responds
with get a 400 response, so that I know the planet_id was invalid.
'''

def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"planet {id} is invalid"}, 400))
    planet= Planet.query.get(id)
    
    # for planet in planets:
    if not planet:
        return abort(make_response({"message": f"planet {id} is not found"}, 404))
    return planet

    
#Get one planet
@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.to_json(), 200)


# UPDATE ONE planet
@planet_bp.route("/<id>", methods = ["PUT"])
def update_one_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()    # would get response body we put int

    planet.title = request_body["title"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()  
    return make_response(f"Planet # {planet.id} successfully updated"), 200

# DELETE ONE Planet
@planet_bp.route("/<id>", methods = ["DELETE"])
def delete_one_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet # {planet.id} successfully deleted"), 200