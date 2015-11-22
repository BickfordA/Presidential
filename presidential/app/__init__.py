
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

#put this at the end to avoid circular references
from app import  views, models
