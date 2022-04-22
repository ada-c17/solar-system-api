from flask import Blueprint


class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.order = order

    planets = [
                Planet(0, "Mercury", "the nearest planet to the Sun", 0)
                Planet(1, "Venus", "named after the Roman goddess of love and beauty", 0)
                Planet(2, "Earth", "Home. the only astronomical object known to harbor life", 1)
                Planet(3, "Mars", "is often called the Red Planet", 2)
                Planet(4, "Jupiter", "more then 2.5 time the mass of all other planets", 79)
                Planet(5, "Saturn", "second-largest planet in the Solar System", 82)
                Planet(6, "Uranus", "named after the Greek god of the sky", 27)
                Planet(7, "Neptune", "the densest giant planet", 14)
                Planet(8, "Pluto", "may or may not be a planet, poor Pluto", 1)
                ]
    planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

    # @planet_bp.route("", methods=["GET"])

# Define a Planet class with the attributes id, name, and description, and one additional attribute
# Create a list of Planet instances