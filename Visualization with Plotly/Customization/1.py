import plotly.graph_objects as pg
import plotly.io as pio

# List all available themes
available_themes = pio.templates
print("Available Plotly Themes:")
print(available_themes)

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]


for theme in available_themes:
    # Create a scatter plot
    fig = pg.Figure(data=pg.Scatter(x=x, y=y, mode='markers', marker=dict(size=10, color='blue')))
    # Apply a theme (e.g., 'plotly_dark')
    fig.update_layout(template=theme, title=f'Scatter Plot with Theme: {theme}')
    # Customize the layout
    # Show the plot
    fig.show()