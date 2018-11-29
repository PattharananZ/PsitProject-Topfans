import pandas as pd
import matplotlib.pyplot as plt

graph = pd.DataFrame( {'Top Fans in Cherprang Fanpage': ['1 Week', '2 Week', '3 Week', '1 Month', '2 Month', '3 Month','4Month'], 'Person TopFans': ['177', '72', '106', '536', '55', '25', '21']})
graph['Person TopFans'] = graph['Person TopFans'].astype(int)

graph.plot(kind='bar', x='Top Fans in Cherprang Fanpage', y='Person TopFans')
plt.xticks(rotation=10)
plt.show()