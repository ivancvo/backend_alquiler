# from flaskr.modelos.modelos import db #importa los modelos 
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
from flaskr import create_app


# import os
# from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

import cloudinary
import cloudinary.uploader
import cloudinary.api


# app = Flask(__name__)
# app.config.from_object(Config)


# cloudinary.config(
#     cloud_name =app.config['CLOUDINARY_CLOUD_NAME'],
#     api_key = app.config['CLOUDINARY_API_KEY'],
#     api_secret = app.config['CLOUDINARY_API_SECRET'] 
# )

# app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
# jwt = JWTManager(app)




# #blueprints
# from .vistas.Vista_Admin import admin_Blueprint
# from .vistas.Vista_Cliente import cliente_blueprint

# app.register_blueprint(admin_Blueprint)
# app.register_blueprint(cliente_blueprint)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config  # Asegúrate de que tu archivo config.py esté en la misma carpeta o en un directorio padre

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


cloudinary.config(
    cloud_name=app.config['CLOUDINARY_CLOUD_NAME'],
    api_key=app.config['CLOUDINARY_API_KEY'],
    api_secret=app.config['CLOUDINARY_API_SECRET']
)

jwt = JWTManager(app)

# Registro de blueprints
from .vistas.Vista_Admin import admin_blueprint


app.register_blueprint(admin_blueprint)


# ... Otras rutas y lógica de tu aplicación

@app.route('/')
def index():
    return '¡preparado para gestionar tus vehiculos?'

if __name__ == '__main__':
    app.run(debug=True)
