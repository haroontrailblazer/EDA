import plotly.graph_objects as pg

Scores=[12, 23, 45, 56, 67, 78, 89, 90, 100, 110, 120, 130, 140, 150]
ages=[10,12,16,18,20,22,24,26,28,30,32,34,36,38]


# Histogram with Scores and Ages
fg=pg.Figure(pg.Histogram(x=Scores, y=ages,name='Scores and Ages', marker_color='red'))
fg.add_trace(pg.Histogram(x=ages, y=Scores, name='Ages and Scores', marker_color='blue'))
fg.update_traces(opacity=0.75)
fg.update_layout(title_text="Histogram with Scores and Ages", xaxis_title_text="Scores", yaxis_title_text="Ages")
fg.show()