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
def two_saved_planets(app):
    # Arrange
    mercury = Planet(
                    name="Mercury",
                    moons=0,
                    description="The first planet.")
    mars = Planet(
                name="Mars",
                moons =2,
                description="The fourth planet.")

    db.session.add_all([mercury, mars])
    # Alternatively, we could do
    # db.session.add(mercury)
    # db.session.add(mars)
    db.session.commit()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_item(empty_list):
    empty_list.append("item")
    return empty_list

def test_len_of_unary_list(one_item):
    assert isinstance(one_item, list)
    assert len(one_item) == 1
    assert one_item[0] == "item"