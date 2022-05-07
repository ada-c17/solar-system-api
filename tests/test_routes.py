from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

   # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Venus",
        "description":"test venus description",
        "moons":2}

def test_get_planet_with_valid_test_data(client,two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
       "id":1,
        "name":"Venus",
        "description":"test venus description",
        "moons":2},
        {"id":2,
        "name":"Mars",
        "description":"test mars description",
        "moons": 3}]

def test_create_one_planet(client):
    #Act
    response = client.post("/planets",json={"name":"New Planet",
        "description":"test new description",
        "moons":3

    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201

def test_get_one_planet_not_exists(client):
    # Act
    response = client.get("/planets/5")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 404
