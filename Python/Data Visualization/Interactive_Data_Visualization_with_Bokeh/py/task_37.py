import numpy as np
from bokeh.models import ColumnDataSource, Button
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, widgetbox

N = 200

x = np.linspace(0, 10, N)
y = np.sin(x) + np.random.random(N)

source = ColumnDataSource(data={
    'x': x, 
    'y': y
})

plot = figure()
plot.circle('x', 'y', source=source)

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)
