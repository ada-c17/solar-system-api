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
    # Arrange
    venus_planet = Planet(id = 1,
                    name="Venus",
                    description="test venus description",
                    moons = 2)
    mars_planet = Planet(id = 2,
                    name="Mars",
                    description="test mars description",
                    moons = 3)

    db.session.add_all([venus_planet, mars_planet])

    db.session.commit()

