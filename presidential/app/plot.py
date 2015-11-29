
def linePlot(dataY, graphName, axisLabel):
    #find the range of the y values
    max = 0;

    for point in dataY:
        if point > max:
            max = point

    xValues = []
    for i in range (0 , max):
        xValues.append(i)
    
    trace = dict(
        x = xValues,
        y = dataY,
        mode = 'lines',
        name = axisLabel,
        line = dict(color = ('rgb(22,96,167)'), width = 4
        )
    )
    
    data = [trace]
    
    layout = dict(
        title = graphName,
        xaxis = dict(title = 'Number'),
        yaxis = dict(title = axisLabel)
    )
    
    fig = dict(data = data, layout = layout)
    
    return fig


# lineData is a dictionary of dictionaries.  Each dictionary in lineData should contain sub-dictionaries named
# 'data', which should be a list of 12 data points,
# 'name', a string which is the name/label for that particular line, and
# 'line', which is a dictionary representing the line's appearance according to Plotly, example:
# line = dict(color = ('rgb(22,96,167)'), width = 4)
def multiLineTimePlot(lineData, graphName, axisLabel):
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
         
    data = []
         
    for ld in lineData:
        trace = dict(
            x = month,
            y = ld['data'],
            name = ld['name'],
            line = ld['line']
        )
        data.append(trace)
        
    layout = dict(
        title = graphName,
        xaxis = dict(title = 'Month'),
        yaxis = dict(title = axisLabel)
    )
    
    fig = dict(data = data, layout = layout)
    
    return fig
