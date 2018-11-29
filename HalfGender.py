import pygal
import pandas as pd
from pygal.style import RotateStyle, LightColorizedStyle

def topfans2():
    """ import data Time to Start a Top Fans Cherprang BNK48 all time from excel by csv file """
    data = pd.read_csv("All Gender.csv")
    dark_rotate_style = RotateStyle('#6495ED', base_style=LightColorizedStyle)
    dark_rotate_style.background = '#B0C4DE'
    dark_rotate_style.plot_background = '#D3D3D3'
    plot_g = pygal.Pie(half_pie=True, interpolate='cubic', style=dark_rotate_style)
    plot_g.title = "Male VS Female Top Fans in Cherprang BNK48 Fanpage (All 992 Person)"
    #plot_g.x_labels = data.TIME
    #plot_g.y_labels = map(int, range(0, 600, 60))
    plot_g.add("Male", data.COUNT)
    plot_g.add("Female", data.COUNT2)
    plot_g.render_to_file("GenderVs.svg")
topfans2()