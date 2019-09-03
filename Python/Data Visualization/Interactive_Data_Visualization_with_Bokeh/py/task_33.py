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

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)
