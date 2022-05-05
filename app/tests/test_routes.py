#`GET` `/planets` returns `200` and an empty array.
def test_get_all_planets_with_no_records(client):
    # ACT
    response = client.get("/planets")
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 200
    assert response_body == []


# GET /planets/1 returns a response body that matches our fixture
def test_get_one_planet(client, two_saved_planets):
    #ACT
    response = client.get("/planets/1")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Mars",
        "description": "Close enough",
        "color": "Red"
    }
    

# GET /planets/1 with no data in test database (no fixture) returns a 404
def test_get_one_planet_but_no_data(client):
    # ACT 
    response = client.get("/planets/1")
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 404
    assert response_body == "Planet 1 does not exist"


# GET /planets with valid test data (fixtures) returns a 200 with
# an array including appropriate test data
def test_get_planets_with_records(client, two_saved_planets):
    # ACT
    response = client.get("/planets")
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 200
    assert response_body == [
                        {
                        "id" : 1,
                        "name": "Mars",
                        "description": "Close enough",
                        "color": "Red"},
                        {
                        "id" : 2,
                        "name": "Earth",
                        "description":"we out here",
                        "color" : "Green"}]


# POST /planets with a JSON request body returns a 201
def test_create_one_planet(client):
    #ACT 
    response = client.post("/planets", json={
        "name": "new planet",
        "description": "with aliens",
        "color": "rainbow"
    })
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 201
    assert response_body == "Planet new planet has been created"