from flask import render_template
from app import app

import sqlfunctions as sql
import plot



@app.route('/')
@app.route('/index')
def index():

    session = sql.newSession()

    cans = sql.candidateNames(session)

    return render_template('index.html',
                            title='Home',
                            candidates = cans)


@app.route('/candidatePage/<canId>')
def candidatePage(canId):
    #create the query session
    session = sql.newSession()

    #get canidates (for nav bar)
    cans = sql.candidateNames(session)

    #get the canidate info for the table
    canInfo = sql.candidateInfo(canId, session)

    #get the canidate name
    candidate_name = sql.candidateName(canId, session)

    #get the google trends
    url = plot.linePlot(sql.canidateGoogleTrend(canId, session), candidate_name, "Google Trends")

    #cadidate top state contributers
    contrib = sql.candidateTopContributionState(canId, session)

    return render_template('candidate.html',
                            title = candidate_name,
                            name = candidate_name,
                            candidates = cans,
                            canInfo = canInfo,
                            graph = url,
                            candidateInfo = canInfo,
                            stateInfo = contrib
                            )
