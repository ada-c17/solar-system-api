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
    blue_planet = Planet(name="Earth",
                    description="watr 4evr",
                    habitable=True)
    red_planet = Planet(name="Mars",
                        description="small and red",
                        habitable=False)

    db.session.add_all([blue_planet, red_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()