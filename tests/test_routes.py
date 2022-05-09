import pytest
from app import create_app
from app import db
from flask.signals import request_finished


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "watr 4evr",
        "habitable" : True
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "small and very cold",
        "habitable" : False
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Pluto successfully created!"