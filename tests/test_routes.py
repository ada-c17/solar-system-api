def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []


def test_get_one_planet(client, save_two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Planet One",
        "description": "gaseous",
        "has_moon": True
    }


def test_planet_id_not_found_in_database_returns_404(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"details": "No planet with id: 1"}


def test_get_all_planets(client, save_two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [
        {"id": 1,
         "name": "Planet One",
         "description": "gaseous",
         "has_moon": True},
        {"id": 2,
         "name": "Planet Two",
         "description": "terrestrial",
         "has_moon": False}
    ]


def test_create_planet(client):
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "gaseous",
        "has_moon": False
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Planet",
        "description": "gaseous",
        "has_moon": False
    }


def test_delete_planet(client, save_two_planets):
    response = client.delete("/planets/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"details": "Planet #2 successfully deleted"}


def test_update_planet(client, save_two_planets):
    response = client.put("/planets/1", json={
        "name": "Updated Planet",
        "description": "terrestrial",
        "has_moon": False
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"details": "Planet #1 successfully updated"}
