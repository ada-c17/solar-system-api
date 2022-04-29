from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLAlchemy_track_modifications"] = False
    app.config["SQLAlchemy_database_uri"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development"

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import planet_bp
    app.register_blueprint(planet_bp)


    return app