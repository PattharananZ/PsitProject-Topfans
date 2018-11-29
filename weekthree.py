import pygal
import pandas as pd
from pygal.style import CleanStyle
def graphy3():
    """ import data male/female from excel by csv file """
    data = pd.read_csv("week3.csv")
    plot_g = pygal.Bar(fill=True, interpolate='cubic', style=CleanStyle)
    plot_g.title = "Top Fans in Week 3"
    plot_g.x_labels = data.GENDER
    plot_g.y_labels = map(int, range(0, 120, 20))
    plot_g.add("Male", data.COUNT)
    plot_g.add("Female", data.COUNT2)
    plot_g.add("Total", data.COUNT3)
    plot_g.render_to_file("plotweek3.svg")
graphy3()