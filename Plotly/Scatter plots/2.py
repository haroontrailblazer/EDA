import plotly.graph_objects as pg
import numpy as np

x=np.random.rand(100)
y=np.linspace(0,10,100)

# Creating a scatter plot with hexagon markers
fg=pg.Figure(data=pg.Scatter(x=x,y=y,mode='markers',marker=dict(symbol='hexagon',size=10,color='pink',line=dict(width=2,color='black'))))

fg.update_layout(title='Hexagon Markers',
                    xaxis_title='X-axis',
                    yaxis_title='Y-axis',
                    font=dict(size=15),
                    width=800,
                    height=500)

fg.show()