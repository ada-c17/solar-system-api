import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

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
def two_saved_planets(app):
    mercury_planet = Planet(title="Mercury", description="Best planet, grey", moons=False)
    venus_planet = Planet(title="Venus", description="Hottest planet", moons=False)

    db.session.add_all([mercury_planet, venus_planet])
    db.session.commit()

@pytest.fixture
def all_planets(app):
    mercury_planet = Planet(title="Mercury", description="Best planet, grey", moons=False)
    venus_planet = Planet(title="Venus", description="Hottest planet", moons=False)
    earth_planet = Planet(title="Earth", description="Our planet", moons=True)
    mars_planet = Planet(title="Mars", description="There's a Rover", moons=True)
    jupiter_planet = Planet(title="Jupiter", description="Big", moons=True)
    saturn_planet = Planet(title="Saturn", description="Has a ring", moons=True)
    uranus_planet = Planet(title="Uranus", description="Far away", moons=True)
    neptune_planet = Planet(title="Neptune", description="So lonely", moons=True)

    db.session.add_all([mercury_planet, venus_planet, earth_planet, mars_planet, jupiter_planet, saturn_planet, uranus_planet, neptune_planet])
    db.session.commit()
