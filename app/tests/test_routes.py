
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Pluto",
            "description": "nobody loves me :(",
            "color": "blue"
        },
        {
            "id": 2,
            "name": "Sun",
            "description": "im hot as heck son",
            "color": "fiery red"
        }
    ]

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "nobody loves me :(",
        "color": "blue"
    }

def test_get_one_planet_with_no_records(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "planet 1 not found"}


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Mars",
        "description": "Is Bruno Mars counted as Mars?",
        "color": "orange"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"
