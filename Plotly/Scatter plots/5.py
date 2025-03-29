import plotly.graph_objects as pg

city=['city1', 'city2', 'city3']
population=[50000, 70000, 30000]
ara=[100, 150, 80]
density=[500000000, 4666000000, 3750000]


# bubble chart
fig=pg.Figure(data=pg.Scatter(x=population, y=ara, mode='markers', text=city, textposition='top center', marker=dict(
    size=density,
    color='yellow',
    sizeref=max(density)/1000,
    sizemin=5,
    sizemode='area',
    opacity=0.9,
    line=dict(width=2, color='black'))))

fig.update_layout(title='City Population Density', xaxis_title='Area (sq km)', yaxis_title='Population Density (people/sq km)')
fig.show()