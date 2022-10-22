import pytest
from app import create_app, db
from app.models.planet import Planet
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_saved_planet(app):
    earth = Planet(name = 'Earth', has_life = True, description = 'Our home.')

    db.session.add(earth)
    db.session.commit()

@pytest.fixture
def three_saved_planets(app):
    earth = Planet(name = 'Earth', has_life = True, description = 'Our home.')
    mars = Planet(name = 'Mars', has_life = True, description = 'Not our home.')
    jupiter = Planet(name = 'Jupiter', has_life = False, description = 'Other place that is not our home.')

    db.session.add_all([earth, mars, jupiter])
    db.session.commit()