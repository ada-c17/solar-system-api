

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_book_by_id(client, two_saved_planets):

    response = client.get('/planets/2')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "Venus",
        "description": "named after the Roman goddess of love and beauty",
        "moons" : 0
    }


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Asimov",
        "description": "This planet named after Isaac Asimov, the other of Lucky Starr book series",
        "moons" : 4
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Asimov successfully created"