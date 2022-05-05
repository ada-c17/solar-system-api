# get all planets (return no records)

from urllib import response


def test_get_all_planets_return_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_return_2(client, saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name":"Uranus",
        "description":"The third-largest planetary radius and fourth-largest planetary mass in the Solar System",
        "length_of_day":"0d 17h 14m"},
        {
        "id":2,
        "name":"Earth",
        "description":"The most beautiful planet",
        "length_of_day":"0d 0h 0m"}]

def test_get_one_planet(client, saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Uranus",
        "description":"The third-largest planetary radius and fourth-largest planetary mass in the Solar System",
        "length_of_day":"0d 17h 14m"
        }

def test_get_one_planet_error(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"planet 1 not found"}

def test_post_one_planet_to_database(client):
    response = client.post("/planets", json={
        "name":"Neptune",
        "description":"The eighth and farthest-known Solar planet from the Sun",
        "length_of_day":"0d 16h 6m"                   
        })
    response_body = response.get_json()
    # response_body = response.get_data(as_text=True)
    # if you want to use line 45, then go to planet_routes.py and then change line 41 to line 42!!

    assert response.status_code == 201
    assert response_body == "Planet Neptune successfully created"
     