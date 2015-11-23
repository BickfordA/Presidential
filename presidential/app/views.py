from flask import render_template
from app import app

import sqlfunctions

@app.route('/')
@app.route('/index')

def index():
    #can = Canidate.query.all()
    #print can

    #Canidate = Table('CANDIDATE', db.Model.metadata, autoload = True, autoload_with = db.engine)

    session = sqlfunctions.newSession()

    cans = sqlfunctions.candidateNames(session)

    return render_template('index.html',
                            title='Home',
                            candidates = cans)

@app.route('/candidatePage/<canId>')
def candidatePage(canId):

    print canId

    canInfo = ""
    candidate_name = "test"

    return render_template('candidate.html',
                            title = candidate_name,
                            canInfo = canInfo
                            )
