import pygal
import pandas as pd
from pygal.style import DarkStyle

def graphy4():
    """ import data male/female from excel by csv file """
    data = pd.read_csv("month1.csv")
    plot_g = pygal.Bar(fill=True, interpolate='cubic', style=DarkStyle)
    plot_g.title = "Top Fans in Last 1 month ago"
    plot_g.x_labels = data.GENDER
    plot_g.y_labels = map(int, range(0, 550, 50))
    plot_g.add("Male", data.COUNT)
    plot_g.add("Female", data.COUNT2)
    plot_g.add("Total", data.COUNT3)
    plot_g.render_to_file("plotmonth1.svg")
graphy4()