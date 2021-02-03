from flask import Flask

# TODO: Import Config Object for Flask Project
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from dealership_api import routes, models