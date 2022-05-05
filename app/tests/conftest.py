
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
    planet_pluto = Planet(name="Pluto",
                        description="nobody loves me :(",
                        color="blue")
    planet_sun = Planet(name="Sun",
                        description="im hot as heck son",
                        color="fiery red")
    db.session.add_all([planet_pluto, planet_sun])
    db.session.commit()
