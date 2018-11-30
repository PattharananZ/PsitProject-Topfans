""" upate bar """
import pandas as pd
import pygal

def graphy():
	""" import data male/female from excel by csv file """
	data = pd.read_csv("update.csv")
	plot_g = pygal.Bar()
	plot_g.title = "Like&Share update"
	plot_g.x_labels = data.DATE
	plot_g.y_labels = map(int, range(1, 40000, 500))
	plot_g.add("LIKE", data.LIKE)
	plot_g.add("SHARE", data.SHARE)
	plot_g.render_to_file("updatebar.svg")
graphy()
