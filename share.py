""" upate bar """
import pandas as pd
import pygal
from pygal.style import LightSolarizedStyle

def graphy():
    """ import data male/female from excel by csv file """
    data = pd.read_csv("update1.csv")
    plot_g = pygal.StackedLine(fill=True, interpolate='cubic', style=LightSolarizedStyle)
    plot_g.title = "Share update"
    plot_g.x_labels = data.DATE
    plot_g.y_labels = map(int, range(0, 4000, 500))
    plot_g.add("SHARE", data.SHARE)
    plot_g.render_to_file("Share.svg")
graphy()
