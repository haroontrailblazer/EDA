import matplotlib.pyplot as mp
import numpy as np 
# Generate random data for scatter plot 
x = np.random.rand(50)  # 50 random values for x-axis 
y = np.random.rand(50)  # 50 random values for y-axis 
# Create the scatter plot 
mp.axhline(0.5,color='r',linewidth=2)
mp.scatter(x, y, color='blue', marker='o') 
# Add labels and title 
mp.xlabel('X-axis') 
mp.ylabel('Y-axis') 
mp.title('Simple Scatter Plot') 
# Display the plot 
mp.show()