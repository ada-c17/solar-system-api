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

    # {
    #     "message": "Planet 1 not found"
    # }