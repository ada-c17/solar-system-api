from urllib import response


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_saved_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Caladan",
        "description": "OG home of House Atreides",
        "moon_count": 4
    },
    {
        "id": 2,
        "name": "Arrakis",
        "description": "Control Arrakis, control the universe",
        "moon_count": 2 
    }]

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Caladan",
        "description": "OG home of House Atreides",
        "moon_count": 4
    }

def test_get_one_missing_planet(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 1 not found"}

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Giedi Prime",
        "description": "Not a great planet",
        "moon_count": 1
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Giedi Prime successfully created"