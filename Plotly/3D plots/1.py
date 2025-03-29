import plotly.graph_objects as pg

x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=[1,2,3,4,5]
fig=pg.Figure(data=[pg.Scatter3d(x=x,y=y,z=z,mode='markers',marker=dict(size=5,color='red',opacity=0.8))])
fig.update_layout(title='3D Scatter plot',scene=dict(xaxis_title='X-axis',yaxis_title='Y-axis',zaxis_title='Z-axis'))
fig.show()