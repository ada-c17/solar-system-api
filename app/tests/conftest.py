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
    earth = Planet(
    name = "Earth",
    description = "Home planet",
    color = "Blue and green"
    )
    mercury = Planet(
        name = "Mercury",
        description = "Smallest planet",
        color = "Blue"
    )
    db.session.add_all([earth, mercury])
    db.session.commit()

