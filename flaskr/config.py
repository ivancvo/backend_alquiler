import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ivanb1227') 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'ivancvo1227')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///alquiler.db')
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME', 'docnct4ym')
    CLOUDINARY_API_KEY= os.getenv('CLOUDINARY_API_KEY', '639257364567225')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET', 'aJWn9YkGF0Q8ITDaeij7A5_YUdE')
    FLASK_RUN_PORT = 5001


if os.environ.get('FLASK_ENV')== 'development':
    pass

if os.environ.get('FLASK_ENV') == 'production':
    pass

