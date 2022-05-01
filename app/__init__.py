from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
<<<<<<< HEAD
=======

db = SQLAlchemy()
migrate = Migrate()
>>>>>>> d5b0ed65df6c5d7d8c660d713c4c1da999dc4699

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
<<<<<<< HEAD
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet
    
=======

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.planet import Planet

>>>>>>> d5b0ed65df6c5d7d8c660d713c4c1da999dc4699
    from .routes import solar_bp
    app.register_blueprint(solar_bp)

    return app

