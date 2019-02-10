from flask import Flask
from app.v1 import v1
from config import config_options

def create_app(config_name):

    app = Flask(__name__)

     # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Registering the blueprint
    app.register_blueprint(v1)
    return app