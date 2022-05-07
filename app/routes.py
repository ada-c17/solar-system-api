from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify,abort, make_response, request
 
planets_bp = Blueprint("planets", __name__, url_prefix="/planets") 

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)
    else:
        planets = Planet.query.all()
    planets_response = []  
    for planet in planets:                                                 
        planets_response.append({                                  
        "id": planet.id,                                   
        "name": planet.name,
      })                                         
    return jsonify(planets_response)  

@planets_bp.route("", methods=[ "POST"])                                               
def create_planet():           
                                              
    request_body = request.get_json()                                          
    new_planet = Planet(                                               
        name = request_body["name"],                                   
        description = request_body["description"],
        moons = request_body["moons"],                         
        )                                      
                        
    db.session.add(new_planet)                                         
    # staging instance new-book                                                
    db.session.commit()                                                
    # commit instance                                          
                            
    return make_response(f"Planet {new_planet.name} created", 201)

 #Get Planet 
@planets_bp.route("/<planet_id>", methods=["GET"])

def get_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    return {   
        "id": planet.id,       
        "name": planet.name,   
        "description": planet.description,     
        "moons":planet.moons
        }


# Update
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet_by_id(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
        
    planet.name = request_body["name"]         
    planet.description = request_body["description"]   
    planet.moons = request_body["moons"]
    db.session.commit()
    return (f"Planet {planet.name} successfully updated.")


# Delete 
@planets_bp.route("/<planet_id>", methods=["DELETE"])

def delete_planet_by_id(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet with id {planet.id} was successfully deleted!")

# Helper Function
def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
            abort(make_response(jsonify(dict(details=f"Invalid Id {id}")), 400))
 

    planet = Planet.query.get(id)
    if planet:
        return planet

    abort(make_response(jsonify(dict(details=f"No planet with id {id} found")), 404))   
