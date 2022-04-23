from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, length_of_day):
        self.id = id
        self.name = name
        self.description = description
        self.length_of_day = length_of_day

planets =  [
    Planet(1, "Mercury", "The closest planet to the Sun, and the smallest planet in our solar system", "58d 15h 30m"),
    Planet(2, "Venus", "The second planet from the Sun and Earth's closest planetary neighbor", "116d 18h 0m"),
    Planet(3, "Mars", "The fourth planet from the Sun and the second-smallest planet in the Solar System", "1d 0h 37m"),
    Planet(4, "Jupiter", "The fifth planet from the Sun and the largest in the Solar System", "0d 9h 56m"),
    Planet(5, "Saturn", "The sixth planet from the Sun and the second-largest in the Solar System, after Jupiter", "0d 10h 42m"),
    Planet(6, "Uranus", "The third-largest planetary radius and fourth-largest planetary mass in the Solar System", "0d 17h 14m"),
    Planet(7, "Neptune", "The eighth and farthest-known Solar planet from the Sun", "0d 16h 6m"),
    Planet(8, "Pluto", "A dwarf planet in the Kuiper belt, after Pluto was discovered in 1930, it was declared the ninth planet from the Sun", "6d 9h 36m")
    ]        

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "length of day": planet.length_of_day
        })
    
    return jsonify(planets_response)