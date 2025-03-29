import plotly.graph_objects as pg

prod=['prod-A','prod-B','prod-C','prod-D','prod-E']
sales=[123, 234, 345, 456, 567]
sales2=[234, 345, 456, 567, 678]
sales3=[345, 456, 567, 678, 789]
sales4=[456, 567, 678, 789, 890]

#Bar plot
fg=pg.Figure(pg.Bar(x=prod, y=sales, name='sales1',marker=dict(color='red',opacity=0.6)))
fg.update_layout(title='Sales by Product', xaxis_title='Product', yaxis_title='Sales')
fg.show()