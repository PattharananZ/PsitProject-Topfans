""" upate bar """
import pandas as pd
import pygal
from pygal.style import LightColorizedStyle

def graphy():
    """ import data male/female from excel by csv file """
    data = pd.read_csv("update1.csv")
    plot_g = pygal.StackedLine(fill=True, interpolate='cubic', style=LightColorizedStyle)
    plot_g.title = "Like update"
    plot_g.x_labels = data.DATE
    plot_g.y_labels = map(int, range(0, 40000,2000))
    plot_g.add("LIKE", data.LIKE)
    plot_g.render_to_file("Like1.svg")
graphy()
