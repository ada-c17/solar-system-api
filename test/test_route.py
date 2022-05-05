

import json


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_by_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "watr 4evr",
        "has_moon": False
    }



def test_get_one_nonexistent_planet_returns_404(client, two_saved_planets):
    # Act
    response = client.get("/planets/8")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
       "details" : 'Invalid id 8'
    }

def test_create_one_planet(client):

    response = client.post("/planets", json={
        "name": "Uros",
        "description": "new",
        "has_moon": True
    })

    response_body = response.get_data(as_text=True)

    #assert 
    assert response.status_code== 201
    assert response_body== "Planet Uros successfully created"