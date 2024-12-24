import pandas as pd 
import numpy as np 
# Creating the DataFrame 
df = pd.DataFrame({ 
'First Name': ['Mina', 'Sima', 'Rima', 'Sita', 'Rita'], 
'Last Name': ['Das', 'Wani', 'Kapur', 'Pande', 'Kumar'], 
'Type': ['Full-time Employee', 'Intern', 'Full-time Employee', 'Part-time Employee', 'Full-time Employee'], 
'Department': ['Administration', 'Technical', 'Administration', 'Technical', 'Management'], 
'YoE': [2, 3, 5, 7, 4], 
'Salary': [20000, 5000, 10000, 10000, 20000] 
}) 
print(df)
# Creating a pivot table 
output = pd.pivot_table(data=df, 
index=['Type'], 
columns=['Department'], 
values='Salary', 
aggfunc='mean') 
print(output) 
# Pivot table with multiple aggfuncs 
output = pd.pivot_table(data=df, 
index=['Type'], 
values='Salary', 
aggfunc=['sum', 'mean', 'count']) 
print(output) 
# Calculate row and column totals (margins) 
output = pd.pivot_table(data=df, 
index=['Type'], 
values='Salary', 
aggfunc=['sum', 'mean', 'count'], 
margins=True, 
margins_name='Grand Total') 
print(output)