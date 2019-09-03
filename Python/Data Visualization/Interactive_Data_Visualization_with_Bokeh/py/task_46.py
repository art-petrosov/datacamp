# Import the necessary modules
from bokeh.io import curdoc
from bokeh.models import CategoricalColorMapper, Slider, ColumnDataSource, HoverTool, Select
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
plot.legend.location = 'top_right'

# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value

    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y

    # Set new_data
    new_data = {
        'x'       : gapminder.loc[yr][x],
        'y'       : gapminder.loc[yr][y],
        'country' : gapminder.loc[yr].Country,
        'pop'     : (gapminder.loc[yr].population / 20000000) + 2,
        'region'  : gapminder.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(gapminder[x])
    plot.x_range.end = max(gapminder[x])
    plot.y_range.start = min(gapminder[y])
    plot.y_range.end = max(gapminder[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr


# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data')

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data')

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country', '@country')])

# Add the HoverTool to the plot
plot.add_tools(hover)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)

# Add the plot to the current document and add the title
curdoc().title = 'Gapminder'

curdoc().add_root(layout)
