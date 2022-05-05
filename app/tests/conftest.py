from unicodedata import name
import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def saved_planets(app):
    # Arrange
    Uranus = Planet(
        name="Uranus",
        description="The third-largest planetary radius and fourth-largest planetary mass in the Solar System",
        length_of_day="0d 17h 14m"
        )
    Earth = Planet(
        name="Earth",
        description="The most beautiful planet",
        length_of_day="0d 0h 0m"
        )

    # db.session.add_all([Uranus, Earth])
    # Alternatively, we could do
    db.session.add(Uranus)
    db.session.add(Earth)
    db.session.commit()
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

