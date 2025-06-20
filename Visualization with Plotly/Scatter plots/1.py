import plotly.graph_objects as pg
import numpy as np

x=np.random.randn(1000)
y=np.random.randn(1000)

fg=pg.Figure(data=pg.Scatter(x=x,y=y,mode='markers',opacity=0.9))
fg.update_layout(title='Scatter plot',xaxis_title='X-axis',yaxis_title='Y-axis')
fg.show()