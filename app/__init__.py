from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
#app.config.from_file('config.py')
db = SQLAlchemy(app)

from app import routes, models
