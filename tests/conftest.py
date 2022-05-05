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
def save_two_planets(app):
    planet_one = Planet(name="Planet One",
                        description="gaseous",
                        has_moon=True)

    planet_two = Planet(name="Planet Two",
                        description="terrestrial",
                        has_moon=False)

    db.session.add_all([planet_one, planet_two])
    db.session.commit()
