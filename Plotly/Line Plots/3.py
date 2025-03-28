import plotly.graph_objects as pg
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

fg= pg.Figure(data=pg.Scatter(x=x, y=y, name='sin(x)'))
fg.add_trace(pg.Scatter(x=x, y=y2, name='cos(x)', line=dict(color='red')))
fg.update_layout(title='Sine Wave', xaxis_title='X-axis', yaxis_title='Y-axis')

# Add annotations to the plot
fg.add_annotation(text='Sine Wave', x=5, y=0, showarrow=True, arrowhead=2, ax=0, ay=-40)
fg.add_annotation(text='Cosine Wave', x=5, y=0, showarrow=True, arrowhead=2, ax=0, ay=-40)