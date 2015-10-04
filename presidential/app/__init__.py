
from flask import Flask

app = Flask(__name__)

#put this at the end to avoid circular references
from app import views
