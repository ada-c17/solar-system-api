import json
from sys import prefix
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color 
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color
        }

planets =[
    Planet(1, "Mercury", "Closest planet to the sun", "grey"),
    Planet(2, "Venus", "Temperatures around 900F", "brown and grey"),
    Planet(3, "Earth", "Only planet currently with life", "blue, brown green, and white"),
    Planet(4, "Mars", "Known as the red and the rusty planet", "red, brown, and tan"),
    Planet(5, "Jupiter", "The king of the solar system", "brown, orange and tan, with white cloud stripes"),
    Planet(6, "Saturn", "The ringed planet.", "golden, brown, and blue-grey"),
    Planet(7, "Uranus", "The planet that spins on it's side", "blue-green"),
    Planet(8, "Neptune", "4x the size of earth and freezing", "blue"),
    Planet(9, "Pluto", "No one can tell me it's not a planet", "blue")
    ]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

#GET all planets
@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets_lists = []
    for planet in planets:
        planets_lists.append(planet.to_json())
    
    return jsonify(planets_lists)