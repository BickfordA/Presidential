from flask import render_template
from app import app

import sqlfunctions
import plot

@app.route('/')
@app.route('/index')
def index():

    session = sqlfunctions.newSession()

    cans = sqlfunctions.candidateNames(session)

    return render_template('index.html',
                            title='Home',
                            candidates = cans)


@app.route('/candidatePage/<canId>')
def candidatePage(canId):

    session = sqlfunctions.newSession()

    #get the canidate info for the table
    canInfo = sqlfunctions.candidateInfo(canId, session)

    #get the canidate name
    candidate_name = sqlfunctions.candidateName(canId, session)

    #get the google trends
    url = plot.linePlot(sqlfunctions.canidateGoogleTrend(canId, session), candidate_name, "Google Trends")

    return render_template('candidate.html',
                            title = candidate_name,
                            name = candidate_name,
                            canInfo = canInfo,
                            graph = url,
                            candidateInfo = canInfo
                            )
