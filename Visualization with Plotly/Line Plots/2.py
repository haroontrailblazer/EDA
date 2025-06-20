import plotly.graph_objects as pg
import numpy as np

x=[110,120,130,140,150,160,170,180,190,200]
y=np.random.randint(0, 500, 10)

fig=pg.Figure(data=pg.Scatter(x=x,y=y))
fig.update_layout(
    title='Simple Line Plot',
    xaxis_title='X-axis',
    yaxis_title='Y-axis',
    showlegend=True
)
fig.show()