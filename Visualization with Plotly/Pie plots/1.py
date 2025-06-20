import plotly.graph_objects as pg

x=['A', 'B', 'C', 'D']
y=[1000,6000,590,7000]

fg=pg.Figure(pg.Pie(values=y, labels=x))
fg.update_layout(title_text='Pie chart')
fg.show()