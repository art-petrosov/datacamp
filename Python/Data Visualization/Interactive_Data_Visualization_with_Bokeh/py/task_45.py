# Import the necessary modules
from bokeh.io import curdoc
from bokeh.models import CategoricalColorMapper, Slider, ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.layouts import row, widgetbox
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

# Make a list of the unique values from the region column: regions_list
regions_list = gapminder.region.unique().tolist()

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

# Add the color mapper to the circle glyph
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'bottom_left'

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # Set the yr name to slider.value and new_data to source.data
    yr = slider.value
    new_data = {
        'x'       : gapminder.loc[yr].fertility,
        'y'       : gapminder.loc[yr].life,
        'country' : gapminder.loc[yr].Country,
        'pop'     : (gapminder.loc[yr].population / 20000000) + 2,
        'region'  : gapminder.loc[yr].region,
    }
    source.data = new_data

    # Add title to figure: plot.title.text
    plot.title.text = 'Gapminder data for %d' % yr


# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country', '@country')])

# Add the HoverTool to the plot
plot.add_tools(hover)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)

# Add the plot to the current document and add the title
curdoc().title = 'Gapminder'

curdoc().add_root(layout)
