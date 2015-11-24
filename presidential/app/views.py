from flask import render_template
from app import app

import sqlfunctions
import plot

import plotly.plotly as py
py.sign_in('db_graph', 'h0px51kava')


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

    session = sqlfunctions.newSession()

    canInfo = ""
    candidate_name = sqlfunctions.candidate_name(canId, session)

    url = plot.linePlot(py, sqlfunctions.canidateGoogleTrend(canId, session), candidate_name)

    return render_template('candidate.html',
                            title = candidate_name,
                            canInfo = canInfo,
                            graph = url
                            )
