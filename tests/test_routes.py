def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == response.get_json()

def test_get_empty_database(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {'message': 'planet 1 not found'}

def test_read_all_planets(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == response.get_json()

def test_create_new_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Jupiter",
        "moons": 53,
        "description": "This is the 6th planet."
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Jupiter successfully created"