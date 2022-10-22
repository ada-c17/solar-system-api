import json

# GET /planets/1 returns a response body that matches our fixture
def test_get_one_planet_successfully(client, one_saved_planet):
    response = client.get('/planets/1')

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Earth',
        'description': 'Our home.',
        'has_life': True
    }


# GET /planets/1 with no data in test database (no fixture) returns a 404
def test_get_one_planet_with_no_fixtures(client):
    response = client.get('/planets/1')

    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "Planet with id of 1 was not found"

# GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_all_planets_successfully(client, three_saved_planets):
    response = client.get('/planets')

    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [{
        'id': 1,
        'name': 'Earth',
        'description': 'Our home.',
        'has_life': True
    }, {
        'id': 2,
        'name': 'Mars',
        'description': 'Not our home.',
        'has_life': True
    }, {
        'id': 3,
        'name': 'Jupiter',
        'description': 'Other place that is not our home.',
        'has_life': False
    }]


# POST /planets with a JSON request body returns a 201
def test_create_planet_successfully(client):
    new_planet = {
        'name': 'Earth',
        'description': 'Our home.',
        'has_life': True
    }
    response = client.post('/planets',data=json.dumps(new_planet),
                headers={"Content-Type": "application/json"})

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"

def test_update_planet_successfully(client, one_saved_planet):
    new_data = {
        'name': 'Earth',
        'description': 'Still our home.',
        'has_life': True
    }
    response = client.put('/planets/1',data=json.dumps(new_data),
                headers={"Content-Type": "application/json"})

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Earth successfully updated"

def test_delete_planet_successfully(client, one_saved_planet):
    response = client.delete('/planets/1')

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Earth successfully deleted"

def test_get_all_planets_can_be_filtered(client, three_saved_planets):
    response = client.get('/planets?has_life=true')

    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [{
        'id': 1,
        'name': 'Earth',
        'description': 'Our home.',
        'has_life': True
    }, {
        'id': 2,
        'name': 'Mars',
        'description': 'Not our home.',
        'has_life': True
    }]