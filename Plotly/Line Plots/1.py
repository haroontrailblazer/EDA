# import plotly
import plotly.graph_objects as pg
import numpy as np

# define data
days=[110,120,130,140,150,160,170,180,190,200]
price=np.random.randint(1,100,10)

# create a line plot
fig=pg.Figure(data=pg.Scatter(x=days,y=price))
fig.show()