

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_book_by_id(client, two_saved_planets):

    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status.code == 200
    assert response_body == {
        "id" : 1,
        "name" : "Mercury",
        "description" : "This is the first planet",
        "moons" : 0
    }
    