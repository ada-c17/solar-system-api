def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "lots of rings",
        "order in solar system": "sixth"
    }

def test_get_one_planet_no_data(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "planet 1 not found"}

def test_get_all_planets_with_data(client, two_saved_planet):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Saturn",
        "description": "lots of rings",
        "order in solar system": "sixth"
    },
    {
        "id": 2,
        "name": "Earth",
        "description": "our planet",
        "order in solar system": "third"
    }]

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Saturn",
        "description": "lots of rings",
        "order in solar system": "sixth"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Saturn successfully created"