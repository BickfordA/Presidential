from flask import render_template
from app import app

import sqlfunctions

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
    #Test Graph
    response = py.plot({
		"data": [{"x":[1, 2, 3],
						"y":[4, 2, 5]
			}], 
			"layout": {
				"title": "hello world"
			}
		}, filename='hello world',
			privacy='public')
    
    #url = "https://plot.ly/~db_graph/19.embed"
    url = response + ".embed"

    print canId

    canInfo = ""
    candidate_name = "test"

    return render_template('candidate.html',
                            title = candidate_name,
                            canInfo = canInfo,
                            graph = url
                            )
