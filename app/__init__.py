from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate() 

def create_app(test_config=None):
    app = Flask(__name__)
    
    # DB config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # handy setting, It means -> I don't wanna hear that message!! 
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development"
    
    db.init_app(app) # saying to SQLalchemy that this is the application you're gonna work with/ the way to get to the database.
    migrate.init_app(app, db) # saying to migrate that this is what I want to work with/the way to get to the database.
    from app.models.planet import Planet

    from app.routes.planet_routes import planets_bp
    app.register_blueprint(planets_bp)
    # from .route import hello_world_bp
    # app.register_blueprint(hello_world_bp)


    return app
