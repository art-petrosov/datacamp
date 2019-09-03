from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from numpy import linspace, sin

x = linspace(0.3, 10, 300)
y = sin(1/x)

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y':y})

# Add a line to the plot
plot = figure()
plot.line('x', 'y', source=source)

slider = Slider(start=1, end=10, value=1, step=1, title='scale')

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)

curdoc().add_root(layout)
