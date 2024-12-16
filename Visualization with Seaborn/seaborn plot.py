import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
# Sample data 
categories = ['A', 'B', 'C', 'D'] 
values = [10, 20, 15, 30] 
df = pd.DataFrame({'Category': categories, 'Values': values}) 
# 1. Scatter Plot 
plt.figure(figsize=(10, 6)) 
sns.scatterplot(x='Category', y='Values', data=df) 
plt.title('Scatter Plot') 
plt.xlabel('Category') 
plt.ylabel('Values') 
plt.show() 
# 2. Line Plot 
plt.figure(figsize=(10, 6)) 
sns.lineplot(x='Category', y='Values', data=df, marker='o') 
plt.title('Line Plot')  
plt.xlabel('Category') 
plt.ylabel('Values') 
plt.show() 
# 3. Bar Plot 
plt.figure(figsize=(10, 6)) 
sns.barplot(x='Category', y='Values', data=df) 
plt.title('Bar Plot') 
plt.xlabel('Category') 
plt.ylabel('Values') 
plt.show()
# 4. Histogram Plot 
plt.figure(figsize=(10, 6)) 
sns.histplot(values, bins=4, kde=True) 
plt.title('Histogram Plot') 
plt.xlabel('Values') 
plt.ylabel('Frequency')  
plt.show() 
# 5. Box Plot 
plt.figure(figsize=(10, 6)) 
sns.boxplot(x='Category', y='Values', data=df) 
plt.title('Box Plot') 
plt.xlabel('Category')  
plt.ylabel('Values') 
plt.show() 
# 6. Heatmap 
# Note: Heatmap usually requires a 2D matrix, here we make a dummy matrix 
import numpy as np 
matrix = np.array([values]) 
plt.figure(figsize=(10, 6)) 
sns.heatmap(matrix, annot=True, cmap='coolwarm', 
xticklabels=categories)  
plt.title('Heatmap') 
plt.xlabel('Category') 
plt.ylabel('Values') 
plt.show() 
# 7. Pair Plot 
# Note: Pair Plot requires at least two numeric columns, using 'Values' twice here 
df_pair = pd.DataFrame({'Values': values, 'Values_Copy': values}) 
plt.figure(figsize=(10, 6)) 
sns.pairplot(df_pair) 
plt.title('Pair Plot') 
plt.show() 
# 8. Violin Plot 
plt.figure(figsize=(10, 6)) 
sns.violinplot(x='Category', y='Values', data=df) 
plt.title('Violin Plot') 
plt.xlabel('Category') 
plt.ylabel('Values') 
plt.show()

