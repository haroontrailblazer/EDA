import plotly.graph_objects as pg

subjects = ['Math', 'Science', 'English', 'History', 'Art']
scores = [[1,2,4,6,8,90,70,60,50,54,45,33,22,85, 90, 78, 88, 92],
          [1,2,4,6,8,90,70,60,50,54,45,33,22,85, 90, 78, 88, 92,80, 85, 75, 82, 89],
          [1,2,4,6,8,90,70,60,50,54,45,33,22,85, 90, 78, 88, 92,78, 80, 70, 75, 85],
          [1,2,4,6,8,90,70,60,50,54,45,33,22,85, 90, 78, 88, 92,90, 92, 88, 95, 91],
          [1,2,4,6,8,90,70,60,50,54,45,33,22,85, 90, 78, 88, 92,95, 98, 92, 94, 97]]

data=zip(subjects, scores)
fg = pg.Figure()
for subject, score in data:
    fg.add_trace(pg.Box(y=score, name=subject))
    fg.update_layout(title='Box Plot of Student Scores', xaxis_title='Subjects', yaxis_title='Scores')
fg.show()