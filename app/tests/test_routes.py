from flask import jsonify, make_response

def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

'''
Create test fixtures and unit tests for the following test cases:

GET /planets/1 returns a response body that matches our fixture  DONE
GET /planets/1 with no data in test database (no fixture) returns a 404  DONE
GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data
POST /planets with a JSON request body returns a 201
'''
def test_get_one_planet_that_matches_our_fixture(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body[0] == {"title": "Mercury", "id": 1, "moons": False, "description": "Best planet, grey"}


def test_get_one_planet_with_no_records(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert response_body == {'message': 'planet 1 is not found'}

def test_get_all_planets_matching_our_fixture(client, all_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == [
        {"title": "Mercury",
        "id": 1,
        "moons": False,
        "description": "Best planet, grey"},
        {"title": "Venus",
        "id": 2,
        "moons": False,
        "description": "Hottest planet"},
         {"title": "Earth",
        "id": 3,
        "moons": True,
        "description": "Our planet"},
         {"title": "Mars",
        "id": 4,
        "moons": True,
        "description": "There's a Rover"},
        {"title": "Jupiter",
        "id": 5,
        "moons": True,
        "description": "Big"},
         {"title": "Saturn",
        "id": 6,
        "moons": True,
        "description": "Has a ring"},
         {"title": "Uranus",
        "id": 7,
        "moons": True,
        "description": "Far away"},
         {"title": "Neptune",
        "id": 8,
        "moons": True,
        "description": "So lonely"}
    ]

def test_post_first_planet(client):
    response = client.post("/planets", json={
            "title": "Mercury",
            "description": "NICE PLANET!!!!!",
            "moons": False})
    response_body = response.get_json()

    return make_response(jsonify(f"Mercury successfully created"), 201)

