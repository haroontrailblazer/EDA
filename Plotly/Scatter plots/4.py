import plotly.graph_objects as pg
import numpy as np

x=np.random.randint(1,50,100)
y=np.random.randn(100)

fig=pg.Figure(data=pg.Scatter(x=x, y=y, mode='markers', marker=dict(size=10, color='purple', symbol='circle')))
fig.update_traces(error_x=dict(type='data', array=[2,2,2,4,2,5,3,3,3,4,1,3,5,3,1,1,3,3,2,2,3,4,3,2,3,4,2,1,3,5,2,2,2,3,4,4,3,2,2,2,1,2,4,3,5,6,1,2,3,3], visible=True))
fig.update_layout(title='Scatter Plot with Error Bars', xaxis_title='X-axis', yaxis_title='Y-axis')
fig.show()