# import pytest

# Create a test to check `GET` `/planets` returns `200` and an empty array.
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get('/planets')
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_with_dummy_records(client, create_two_planets):
    # Act
    response = client.get('/planets/1')
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "smallest planet",
        "color": "magenta"
    }

def test_get_one_planet_with_no_records(client):
    # Act
    response = client.get('/planets/1')
    response_body = response.get_json()

    #assert
    assert response.status_code == 404
    assert response_body == None

def test_create_one_planet(client):
    # Act
    response = client.post('/planets', json={
        "name": "Venus",
        "description": "Planet of love",
        "color": "hot pink"
    })
    response_body = response.get_json()

    #assert
    assert response.status_code == 201
    assert response_body == "Planet Venus successfully created"

def test_replace_one_planet(client, create_two_planets):
    # Act
    response = client.put('/planets/1', json={
        "name": "Earth",
        "description": "Home for humans",
        "color": "blueish green"
    })
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == "Planet 1 was successfully replaced."

def test_delete_one_planet(client, create_two_planets):
    # Act
    response = client.delete('/planets/1')
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == 'Planet 1 successfully deleted'