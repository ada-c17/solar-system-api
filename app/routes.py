
from flask import Blueprint, request, make_response
from app import db
from app.models.planet import Planet


solar_bp = Blueprint("planets", __name__, url_prefix="/planets")

@solar_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(id = request_body['id'],
                        name = request_body['name'],
                        description = request_body['description'],
                        color = request_body['color']
                        )
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created, 201")

