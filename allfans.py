import pygal
import pandas as pd
from pygal.style import DefaultStyle

def topfans():
    """ import data Time to Start a Top Fans Cherprang BNK48 all time from excel by csv file """
    data = pd.read_csv("All Top Fans.csv")
    plot_g = pygal.Bar(fill=True, interpolate='cubic', style=DefaultStyle)
    plot_g.title = "Time to start a Top Fans in Cherprang BNK48 Fanpage"
    plot_g.x_labels = data.TIME
    plot_g.y_labels = map(int, range(0, 600, 60))
    plot_g.add("1 Week", data.COUNT)
    plot_g.add("2 Week ", data.COUNT2)
    plot_g.add("3 Week", data.COUNT3)
    plot_g.add("1 Month", data.COUNT4)
    plot_g.add("2 Month", data.COUNT5)
    plot_g.add("3 Month", data.COUNT6)
    plot_g.add("4 Month", data.COUNT7)
    plot_g.render_to_file("Alltopfans.svg")
topfans()