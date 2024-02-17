from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_restx import Api
from flask_injector import FlaskInjector
from app.config import Config

# Create a Flask app
app = Flask(__name__)
# Load configurations
app.config.from_object(Config)

# Enable CORS
CORS(app)

api = Api(app, version='1.0', title='API', description='API for the backend')
# Enable Swagger
Swagger(app)

# Import the routes
from app.Presentation.UserInformationController import api as user_information_ns
api.add_namespace(user_information_ns)

# Dependency injection
FlaskInjector(app=app)