import pygal
import pandas as pd
from pygal.style import LightColorizedStyle

def graphy7():
    """ import data male/female from excel by csv file """
    data = pd.read_csv("month4.csv")
    plot_g = pygal.Bar(fill=True, interpolate='cubic', style=LightColorizedStyle)
    plot_g.title = "Top Fans in Last 4 month ago"
    plot_g.x_labels = data.GENDER
    plot_g.y_labels = map(int, range(0, 30, 3))
    plot_g.add("Male", data.COUNT)
    plot_g.add("Female", data.COUNT2)
    plot_g.add("Total", data.COUNT3)
    plot_g.render_to_file("plotmonth4.svg")
graphy7()