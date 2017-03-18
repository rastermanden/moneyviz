import pandas as pd
from bokeh.charts import Horizon, output_file, show
from bokeh.plotting import figure
from bokeh.embed import components
# read in some stock data from the Yahoo Finance API

dateparse = lambda x: pd.datetime.strptime(x, '%Ym%m')
df = pd.read_csv("data.csv", sep=';', parse_dates=['TID'], date_parser=dateparse)
#print df

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(plot_width=822, plot_height=400,title="Danmarks Statsgaeld", x_axis_type="datetime", x_axis_label='Periode' , y_axis_label='MIA')

# add a line renderer with legend and line thickness
p.line(df['TID'], df['INDHOLD'], legend="Gaeld.", line_width=2)

# show the results
show(p)

script, div = components(p)
print script
print div