from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request , abort
from app.models.moon import Moon
from .moon_helpers import validate_moon


moon_bp = Blueprint("moon_bp", __name__, url_prefix="/moons")


# CREATE Moon
@moon_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()

    new_moon = Moon.create(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} has been successfully created!",201)

# GET ALL Moons
@moon_bp.route("", methods=["GET"])
def read_all_moons():
    name_query = request.args.get("name")

    if name_query:
        moons = Moon.query.filter_by(name =name_query)
    else:
        moons = Moon.query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_json())

    return jsonify(moons_response), 200

# GET one Moon
@moon_bp.route("/<id>", methods = ["GET"])
def read_one_moon(id):
    moon = validate_moon(id)
    return jsonify(moon.to_json()), 200

@moon_bp.route("/<id>", methods = ["PUT"])
def update_one_moon(id):
    moon = validate_moon(id)
    request_body = request.get_json()

    moon.update(request_body)

    db.session.commit()
    return make_response(f"Moon #{moon.id} successfully updated"), 200

@moon_bp.route("/<id>", methods = ["DELETE"])
def delete_one_moon(id):
    moon = validate_moon(id)
    db.session.delete(moon)
    db.session.commit()

    return make_response(f"Moon #{moon.id} successfully deleted"), 200
