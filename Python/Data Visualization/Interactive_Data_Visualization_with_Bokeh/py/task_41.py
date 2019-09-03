# Import the necessary modules
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd

gapminder = pd.read_csv('Interactive_Data_Visualization_with_Bokeh/csv/gapminder_tidy.csv', index_col='Year')

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : gapminder.loc[1970].fertility,
    'y'       : gapminder.loc[1970].life,
    'country' : gapminder.loc[1970].Country,
    'pop'     : (gapminder.loc[1970].population / 20000000) + 2,
    'region'  : gapminder.loc[1970].region,
})

# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = min(gapminder.fertility), max(gapminder.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = min(gapminder.life), max(gapminder.life)

# Create the figure: plot
plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700, x_range=(xmin, xmax), y_range=(ymin, ymax))

# Add circle glyphs to the plot
plot.circle(x='x', y='y', fill_alpha=0.8, source=source)

# Set the x-axis label
plot.xaxis.axis_label ='Fertility (children per woman)'

# Set the y-axis label
plot.yaxis.axis_label = 'Life Expectancy (years)'

# Add the plot to the current document and add a title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'
