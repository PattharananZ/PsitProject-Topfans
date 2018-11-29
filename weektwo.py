import pygal
import pandas as pd
from pygal.style import LightSolarizedStyle

def graphy2():
    """ import data male/female from excel by csv file """
    data = pd.read_csv("week2.csv")
    plot_g = pygal.Bar(fill=True, interpolate='cubic', style=LightSolarizedStyle)
    plot_g.title = "Top Fans in Week 2"
    plot_g.x_labels = data.GENDER
    plot_g.y_labels = map(int, range(0, 80, 10))
    plot_g.add("Male", data.COUNT)
    plot_g.add("Female", data.COUNT2)
    plot_g.add("Total", data.COUNT3)
    plot_g.render_to_file("plotweek2.svg")
graphy2()