from flask import render_template
from app import app
from app import db

from sqlalchemy.orm import create_session

from .models import Candidate

@app.route('/')
@app.route('/index')

def index():
    #can = Canidate.query.all()
    #print can

    #Canidate = Table('CANDIDATE', db.Model.metadata, autoload = True, autoload_with = db.engine)

    session = create_session(bind = db.engine)

    canidates = session.query(Candidate).all()

    return render_template('index.html',
                            title='Home',
                            canidates = canidates)
