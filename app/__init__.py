from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

db = SQLAlchemy()
# creating new db object
migrate = Migrate()
load_dotenv()



def create_app(testing = None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['CORS_HEADERS'] = 'Content-Type'
    if testing is None:  
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TESTING_SQLALCHEMY_DATABASE_URI')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')


    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    #hooking up db and app
    migrate.init_app(app, db)

    from .models.cars import Car

    from .routes.cars import cars_bp
    app.register_blueprint(cars_bp)

    return app