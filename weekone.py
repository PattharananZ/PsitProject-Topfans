import pygal
import pandas as pd
from pygal.style import DarkSolarizedStyle

def graphy():
	""" import data male/female from excel by csv file """
	data = pd.read_csv("week1.csv")
	plot_g = pygal.Bar(fill=True, interpolate='cubic', style=DarkSolarizedStyle)
	plot_g.title = "Top Fans in Week 1 "
	plot_g.x_labels = data.GENDER
	plot_g.y_labels = map(int, range(1, 180, 20))
	plot_g.add("Male", data.COUNT)
	plot_g.add("Female", data.COUNT2)
	plot_g.add("Total", data.COUNT3)
	plot_g.render_to_file("plotweek1.svg")
graphy()
