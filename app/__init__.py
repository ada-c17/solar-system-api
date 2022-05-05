from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os #provide a way to read env variables


db = SQLAlchemy()
migrate = Migrate() 
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    
    # DB config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # handy setting, It means -> I don't wanna hear that message!!
    if not test_config: 
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    
    db.init_app(app) # saying to SQLalchemy that this is the application you're gonna work with/ the way to get to the database.
    migrate.init_app(app, db) # saying to migrate that this is what I want to work with/the way to get to the database.
    from app.models.planet import Planet

    from app.routes.planet_routes import planets_bp
    app.register_blueprint(planets_bp)
    # from .route import hello_world_bp
    # app.register_blueprint(hello_world_bp)


    return app
