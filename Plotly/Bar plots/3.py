import plotly.graph_objects as pg
month=['Jan','Feb','Mar','Apr','May']
prod=['prod-A','prod-B','prod-C','prod-D','prod-E']
sales=[[123, 234, 345, 456, 567],[234, 345, 456, 567, 678],[345, 456, 567, 678, 789],[456, 567, 678, 789, 890],[567, 678, 789, 890, 901]]

# Grouped Horizontal Bar plot
fg=pg.Figure()
for i,product in enumerate(prod):
    fg.add_trace(pg.Bar(y=sales[i], x=month, orientation="h", name=product))
    fg.update_layout(barmode='group',title='Sales by Month', xaxis_title='Month', yaxis_title='Sales')
    fg.show()