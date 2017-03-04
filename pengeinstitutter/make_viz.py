#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from bokeh.charts import Horizon, output_file, show
from bokeh.plotting import figure

# read in some stock data from the Yahoo Finance API

dateparse = lambda x: pd.datetime.strptime(x, '%Ym%m')
df = pd.read_csv("data.csv", sep=';', parse_dates=['TID'], date_parser=dateparse, na_values='..')
AZZ = df[df['BRANCHE'] == "AZZ"] #Landbrug, skovbrug og fiskeri.
BZZ = df[df['BRANCHE'] == "BZZ"] #Råstofindvinding
CZZ = df[df['BRANCHE'] == "CZZ"] #Fremstillingsvirksomhed
# output to static HTML file
output_file("lines.html")
#print df
# create a new plot with a title and axis labels
p = figure(plot_width=800,title="DNPUDDKB: INDENLANDSK UDLÅN FRA PENGEINSTITUTTER EFTER BRANCHE i DKK", x_axis_type="datetime", x_axis_label='Periode' , y_axis_label='Ultimobalance (mio. kr.)')

# add a line renderer with legend and line thickness
p.line(AZZ['TID'], AZZ['INDHOLD'], legend="Landbrug, skovbrug og fiskeri.", line_width=2)
p.line(BZZ['TID'], BZZ['INDHOLD'], legend="Råstofindvinding", line_width=2,line_color='orange')
p.line(CZZ['TID'], CZZ['INDHOLD'], legend="Fremstillingsvirksomhed", line_width=2,line_color='red')

# show the results
show(p)