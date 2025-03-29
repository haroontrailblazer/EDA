import plotly.graph_objects as pg

# Data for the 3D line plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
z = [5, 15, 25, 35, 45]

# Creating a 3D line plot
fig = pg.Figure(data=[pg.Scatter3d(
    x=x,  # X-axis data
    y=y,  # Y-axis data
    z=z,  # Z-axis data
    mode='lines',  # Line plot mode
    line=dict(color='blue', width=4)  # Line style
)])

# Updating the layout with title and axis labels
fig.update_layout(
    title='3D Line Plot',
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis'
    )
)

# Displaying the plot
fig.show()