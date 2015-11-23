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

    candidates = session.query(Candidate.Candidate_id, Candidate.Fname, Candidate.Lname).all()

    parsed = []
    for can in candidates:
        pc =[]
        pc.append(can[0])
        pc.append(str(can[1].encode('ascii', 'ignore') + " " + can[2].encode('ascii', 'ignore')))
        parsed.append(pc)

    'Some String'.encode('ascii', 'ignore')

    return render_template('index.html',
                            title='Home',
                            candidates = candidates)

@app.route('/candidatePage/<canId>')
def candidatePage(canId):

    print canId

    canInfo = ""
    candidate_name = "test"

    return render_template('candidate.html',
                            title = candidate_name,
                            canInfo = canInfo
                            )
