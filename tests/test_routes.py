
#test get all palnets returns a 200 with an array including appropriate test data
def test_get_all_planets_with_empty_db_return_empty_list(client):
    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

#test returns a reponse body that matches our fixture for planet id  
def test_get_one_planet_by_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "mars",
        "description": "watr 4evr",
        "has_moon": True
    }

#test that no data in test returns 404 for planet id
def test_no_data_in_test_db_returns_404(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
       "details" : 'Invalid planet 3'
    }
    
#create planet by id with JSON request body returns a 201
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Neptune",
        "description": "Gaseous",
        "has_moon" : True
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Neptune has been created"



