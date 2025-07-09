import plotly.graph_objects as pg

# Data for the 3D line plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
z = [5, 15, 25, 35, 45]

# Creating a 3D line plot
fig = pg.Figure(data=[pg.Scatter3d(x=x,y=y,z=z,mode='lines',line=dict(color='blue', width=4))])

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