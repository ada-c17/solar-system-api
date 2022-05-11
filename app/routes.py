from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
from app.models.helpers import validate_planet


planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

# CREATE PLANET
@planets_bp.route("", methods = ["POST"])
def create_planet():
	request_body = request.get_json()
	
	new_planet = Planet.create(request_body)

	db.session.add(new_planet)
	db.session.commit()

	return jsonify(f"Planet {new_planet.name} has been successfully created"), 201 #use make response when you want to return something that is not json

# GET ALL
@planets_bp.route("", methods = ["GET"])
def get_all_planets():

	days_query = request.args.get("length_of_year")
	name_query = request.args.get("name")
	description_query = request.args.get("description")
	circumference_query = request.args.get("circumference")

	if days_query:
		planets = Planet.query.filter_by(length_of_year = days_query)
	elif name_query:
		planets = Planet.query.filter_by(name = name_query)
	elif description_query:
		planets = Planet.query.filter_by(description = description_query)
	elif circumference_query:
		planets = Planet.query.filter_by(circumference = circumference_query)
	else:
		planets = Planet.query.all()

	planets_response = []
	
	for planet in planets:
		planets_response.append(planet.to_json())
			
	return jsonify(planets_response)

# GET ONE PLANET
@planets_bp.route("/<id>", methods = ["GET"])
def get_one_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_json()), 200




	# {
	# 	name:
	# 	description:
	# 	circumference:
	# 	length_of_year:
    # }

#PUT or update ONE PLANET
@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.update(request_body)
    # planet.name = request_body["name"]
    # planet.description = request_body["description"]
    # planet.circumference = request_body["circumference"]
    # planet.length_of_year = request_body["length_of_year"]

    db.session.commit()

    return make_response(f"Planet #{id} succesffully updated"), 200

#MAKE PATCH REQUEST

#DELETE ONE PLANET
@planets_bp.route("/<id>", methods=["DELETE"])
def delete_one_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{id} was successfully deleted"), 200
	# 	{"name": "Mercury",
	# 	"description": "made mostly of rocks",
	# 	"circumference": 9522,
	# 	"length_of_year": 88
    # }

	
	# {
	# 	"name": Venus,
	# 	"description": most like Earth,
	# 	"circumference": 23617,
	# 	"length_of_year": 225
    # }
	

	# {
	# 	"name": "Earth"
	# 	"description": "you are here"
	# 	"circumference": 24889
	# 	"length_of_year": 365
    # }


	# {
	# 	"name": "Mars",
	# 	"description": "the red planet",
	# 	"circumference": 13256,
	# 	"length_of_year": 687
    # }


	# {
	# 	"name": "Jupiter",
	# 	"description": "largest planet",
	# 	"circumference": 278985,
	# 	"length_of_year": 4320
    # }


	# {
	# 	"name": "Saturn",
	# 	"description": "sun's bae with all 7 rings",
	# 	"circumference": 235185,
	# 	"length_of_year": 10620
    # }


	# {
	# 	"name": "Uranus",
	# 	"description": "can only be seen with a telescope",
	# 	"circumference": 99739,
	# 	"length_of_year": 30240
    # }


	# {
	# 	"name": "Neptune",
	# 	"description": "it is an intense blue color",
	# 	"circumference": 96645,
	# 	"length_of_year": 59400
    # }


	# {
	# 	"name": "Pluto",
	# 	"description": "no dwarf in my book",
	# 	"circumference": 7144,
	# 	"length_of_year": 88920
    # }
