

def linePlot(py, dataX, name):
    #find the range of the x values
    max = 0;

    for point in dataX:
        if point > max:
            max = point

    yValues = []
    for i in range (0 , max):
        yValues.append(i)
    
    #Test Graph
    response = py.plot({
    	"data": [{"x":yValues,
    					"y":dataX
    		}],
    		"layout": {
    			"title": name
    		}
    	}, filename= (name + 'line_plot'),
    		privacy='public')
    '''
    #Test Graph
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
         
    poll = [5, 8, 12, 16, 19, 28, 22, 19, 25, 7, 13, 21]
    
    tweets = [200, 250, 150, 225, 220, 175, 150, 50, 75, 125, 200]
    
    trace0 = go.Scatter(
        x = month,
        y = poll,
        name = 'Opinion Polls',
        line = dict(color = ('rgb(22,96,167)'), width = 4
        )
    )
    
    trace1 = go.Scatter(
        x = month,
        y = tweets,
        name = 'Twitter Activity',
        line = dict(color = ('rgb(205, 12, 24)'), width = 4
        )
    )
    
    data = [trace0, trace1]
    
    layout = dict(
        title = 'Candidate No.' + str(canId),
        xaxis = dict(title = 'Month'),
        yaxis = dict(title = 'Stuff')
    )
    
    fig = dict(data = data, layout = layout)
    
    response = py.plot(
        fig, 
        filename='Candidate No.' + str(canId),
		privacy='public')
    
    url = response + ".embed"
    '''
    url = response + ".embed"
    return url
