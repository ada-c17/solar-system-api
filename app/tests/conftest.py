import pytest
from app.models.planet import Planet
from app import create_app
from app import db
from flask.signals import request_finished


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    # everytime you finish a request this removes any saved data (like cleaning our a cache)
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
    mercury = Planet(name="Mercury",
    description="made mostly of rocks", circumference=9522, length_of_year = 88)
    venus = Planet(name="Venus",
    description="most like Earth", circumference=23617, length_of_year=225)

    db.session.add_all([mercury, venus])
    # Alternatively, we could do# db.session.add(mercury)# db.session.add(venus)
    db.session.commit()
