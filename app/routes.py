from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, name, id, description, color):
#         self.name = name
#         self.id = id
#         self.description = description
#         self.color = color


# planets = [
#     Planet("Earth", 3, "Earth is the 3rd planet in solar system", "blue"),
#     Planet("Mars", 4, "Mars is the 4th planet in solar system", "red"),
#     Planet("Jupiter", 5, "Jupiter is the 5th planet in solar system", "tan")
# ]

# def validate_planet(id):
#     try:
#         id = int(id)
#     except:
#         return abort(make_response({"message": f"planet {id} is invalid"}, 400))
#     for planet in planets :
#         if planet.id == id:
#             return jsonify(planet.to_json()), 200
#     return abort(make_response({"message": f"planet {id} is not found"}, 404))
# first string is flask blueprint name
# run in localhost need to add/planets at the end
solar_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @solar_bp.route("", methods=["GET"])
# def see_planets():
# all_planets = []
    # for planet in planets:
    #     all_planets.append(
    #         {"Name": planet.name,
    #          "ID": planet.id,
    #          "Description": planet.description,
    #          "Color": planet.color}
    #     )
    # return jsonify(all_planets), 200


@solar_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method== "POST":
        request_body=request.get_json()
        new_planet=Planet(
            id=request_body["id"],
            name=request_body["name"],
            color=request_body["color"],
            description=request_body["description"])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

    elif request.method== "GET":
        planets=Planet.query.all()
        planets_response=[]
        for planet in planets:
            planets_response.append(
                    {"Name": planet.name,
                    "ID": planet.id,
                    "Description": planet.description,
                    "Color": planet.color})
        return jsonify(planets_response), 200

        
