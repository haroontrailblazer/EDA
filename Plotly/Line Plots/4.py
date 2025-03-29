import plotly.graph_objects as pg
import numpy as np

x = np.linspace(0, 1, 1000)
y1 = np.sin(x)

fg= pg.Figure(data=pg.Scatter(x=x,y=y1,name='sin(x)'))
fg.update_layout(title='Line Plot with Shapes',xaxis_title='X-axis',yaxis_title='Y-axis')
fg.add_annotation(text='sin(x)',x=0.5,y=0.5,showarrow=True,arrowhead=2,ax=20,ay=-30)
fg.add_shape(type='rect',x0=0.2,x1=0.5,y0=-0.5,y1=0.5,fillcolor='yellow',opacity=0.2,line=dict(width=0.1))
fg.show(),