

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

    #url = "https://plot.ly/~db_graph/19.embed"
    url = response + ".embed"
    return url
