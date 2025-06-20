import plotly.graph_objects as pg

data_matrix = [
    [1, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
]
# This is a 4x4 matrix with values ranging from 1 to 160
fig = pg.Figure(data=pg.Heatmap(z=data_matrix,colorscale='blues'))
# The colorscale is set to 'blues', which is a perceptually uniform colormap
# that is good for displaying data in heatmaps.
fig.update_layout(title='Basic Heatmap', xaxis_title='X Axis', yaxis_title='Y Axis')
fig.show()