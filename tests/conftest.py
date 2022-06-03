import pytest
from flask import request_finished
from app import create_app, db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    #make sure we have everything we need and yield app
    with app.app_context():
        db.create_all()
        yield app

    #this will clean everything up
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()




@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mars_planet = Planet(name="mars",
                      description="watr 4evr", has_moon=True)
    venus_planet = Planet(name="venus",
                         description="i luv 2 climb rocks", has_moon=True)

    db.session.add_all([mars_planet, venus_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit
