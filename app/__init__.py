from flask import Flask
frpm flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(pymeetup)

from app import routes, models
