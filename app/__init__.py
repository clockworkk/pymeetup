from flask import Flask
### 2015-01-25 -- blingall -- Flask changed how they do shit
###from flask.ext.sqlalchemy import SQLAlchemy

## You must have Flask-SQLAlchemy installed as well
#- use pip
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
#app.config.from_file('config.py')
db = SQLAlchemy(app)

from app import routes, models, parse
