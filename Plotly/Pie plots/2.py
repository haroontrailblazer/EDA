import plotly.graph_objects as pg

x=['A', 'B', 'C', 'D']
y=[1000,6000,590,7000]

fg=pg.Figure(pg.Pie(values=y, labels=x,hole=0.5,marker=dict(colors=['#FF0000','#00FF00','#0000FF','#FFFF00'])))
fg.update_layout(title_text='Pie chart With Hole')
fg.show()