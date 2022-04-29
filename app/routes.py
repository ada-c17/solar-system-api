from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color 

#     def to_dict(self):
#         return dict(
#         id=self.id,
#         name=self.name,
#         description=self.description,
#         color=self.color,
#         )

# planets = [
#     Planet(1, "Mercury", "Super small, comparatively", "slate gray"),
#     Planet(2, "Venus", "It's sooo hot!", "yellow-white"),
#     Planet(3, "Earth", "Home to humans", "blue-green"),
#     Planet(4, "Mars", "The red one", "red"),
#     Planet(5, "Jupiter", "The biggest of them all", "orange-yellow"),
#     Planet(6, "Saturn", "What beautiful rings it has!", "hazy yellow-brown"),
#     Planet(7, "Uranus", "Tilted sideways", "blue-green"),
#     Planet(8, "Neptune", "Giant, stormy, blue", "blue"),
#     Planet(9, "Maybe Pluto", "Is it really a planet??", "reddish-brown")
#     ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        color = request_body["color"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return f"Planet {new_planet.name} successfully created", 201

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }
        )
    return jsonify(planets_response)

# def validate_planet(id):
#     try:
#         id = int(id)
#     except ValueError:
#         abort(make_response({"message":f"invalid id: {id}"}, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet

#     abort(make_response({"Message":f"Planet ID {id} not found"}, 404))

# @bp.route("", methods=["GET"])
# def get_planets():
#     results_list = []
#     for planet in planets:
#         results_list.append(planet.to_dict())
#     return jsonify(results_list)

# @bp.route("/<id>", methods=["GET"])
# def get_planet(id):
#     planet = validate_planet(id)
#     return planet.to_dict(), 200
