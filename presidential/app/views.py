from flask import render_template
from app import app

import sqlfunctions as sql
import plot
import json



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
    fig = plot.linePlot(sql.canidateGoogleTrend(canId, session), candidate_name, "Google Trends")
    
    graphData = json.dumps(fig['data'])
    graphLayout = json.dumps(fig['layout'])
    print(graphData)
    print(graphLayout)

    #cadidate top state contributers
    contrib = sql.candidateTopContributionState(canId, session)

    return render_template('candidate.html',
                            title = candidate_name,
                            name = candidate_name,
                            candidates = cans,
                            canInfo = canInfo,
                            data = graphData,
                            layout = graphLayout,
                            candidateInfo = canInfo,
                            stateInfo = contrib
                            )
