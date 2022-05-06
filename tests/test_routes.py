# from hello-books

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_handle_teapot(client):
    response = client.get("/planets/teapot")

    assert response.status_code == 418

def test_get_one_planet(client, two_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 3,
        "name": "Earth",
        "order_from_sun": 3,
        "description": "something about earth",
        "gravity": "9.81 m/s2"
    }

def test_get_invalid_planet(client):
    response = client.get("planets/12")
    response_body = response.get_json()

    assert response.status_code == 404


