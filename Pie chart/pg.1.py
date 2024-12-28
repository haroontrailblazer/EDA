import matplotlib.pyplot as mp
mp.style.use('dark_background')
marks = [10, 20, 30, 40, 50]
subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'Computer']
mp.pie(marks, labels=subjects)
mp.show() 