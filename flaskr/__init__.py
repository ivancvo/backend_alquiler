from flask import Flask

def create_app(config_name):
    app= Flask(__name__)
    app.config['SECRET_KEY'] = 'ivanbedoya'
    app.config['JWT_SECRET_KEY'] = 'bedoya1227'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alquiler.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_RUN_PORT'] = 5001

    return app