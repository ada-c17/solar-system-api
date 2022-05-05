def test_get_all_planets_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()
    assert response.status_code == 404
    assert response_body == {'message': 'Planet 1 does not exist'}

def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == {
    "id": 1,
    "name":"Earth",
    "description" : "Home planet",
    "color" : "Blue and green"
    }

def test_get_all_planets(client,two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert {"id": 1, 
            "name": "Earth",
            "description":"Home planet",
            "color":"Blue and green"} in response_body
    assert {"id": 2,
            "name":"Mercury",
            "description":"Smallest planet",
            "color":"Blue"} in response_body

def test_create_one_planet(client):
    response = client.post("/planets", json = {
        "name": "Mars",
        "description": "dusty, cold, desert world", 
        "color": "red"
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "planet 1 successfully created"
