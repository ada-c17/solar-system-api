from flask import Blueprint, jsonify, make_response, abort, request
from app.models.moon import Moon

def validate_moon(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"moon {id} is invalid"}, 400))
    moon= Moon.query.get(id)

    if not moon:
        return abort(make_response({"message": f"moon {id} is not found"}, 404))

    return moon
