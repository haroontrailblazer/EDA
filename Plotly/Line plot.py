import plotly.graph_objs as go
from plotly.offline import plot

# Define the data for the line plot
trace = go.Scatter(
    x=[1, 2, 3, 4, 5],  # X-axis values
    y=[10, 14, 12, 15, 13],  # Y-axis values
    mode='lines+markers',  # Line with markers
    name='Line Plot',  # Legend name
    line=dict(color='blue', width=2),  # Line style
    marker=dict(size=8)  # Marker style
)

# Define the layout for the plot
layout = go.Layout(
    title='Interactive Line Plot',  # Plot title
    xaxis=dict(title='X-axis Label'),  # X-axis label
    yaxis=dict(title='Y-axis Label'),  # Y-axis label
    hovermode='closest'  # Enable hover interaction
)

# Combine the data and layout into a figure
fig = go.Figure(data=[trace], layout=layout)

# Render the plot in the browser
plot(fig, filename='interactive_line_plot.html', auto_open=True)