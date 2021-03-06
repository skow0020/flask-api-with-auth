from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from resources.errors import errors
from database.db import initialize_db

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)

# imports requiring app and mail
from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

initialize_db(app)
initialize_routes(api)
jwt = JWTManager(app)
