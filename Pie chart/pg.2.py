import matplotlib.pyplot as mp
mp.style.use('dark_background')
subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'Computer','Avg']
marks = [10, 20, 30, 40, 50,100]
mp.pie(marks,labels=subjects,autopct='%0.1f%%')
mp.title('Marks of Students')
mp.show()