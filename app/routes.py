from flask import Blueprint, jsonify


class Planet:
    def __init__(self, name, id, description, color):
        self.name = name
        self.id = id
        self.description = description
        self.color = color


planets = [
    Planet("Earth", 3, "Earth is the 3rd planet in solar system", "blue"),
    Planet("Mars", 4, "Mars is the 4th planet in solar system", "red"),
    Planet("Jupiter", 5, "Jupiter is the 5th planet in solar system", "tan")
]

# first string is flask blueprint name
# run in localhost need to add/planets at the end
solar_bp = Blueprint("", __name__, url_prefix="/planets")


@solar_bp.route("", methods=["GET"])
def see_planets():
    all_planets = []
    for planet in planets:
        all_planets.append(
            {"Name": planet.name,
             "ID": planet.id,
             "Description": planet.description,
             "Color": planet.color}
        )
    return jsonify(all_planets), 200
