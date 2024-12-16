# Import the necessary libraries 
import matplotlib.pyplot as plt     
import numpy as np                  
# For creating and displaying plots 
# For numerical operations and generating data 
# Generate 10 evenly spaced values between -1 and 1 
x = np.linspace(-1, 1, 10) 
# Print the generated x values to verify them 
print(x) 
# Compute the y values using the linear function y = 2 * x + 1 
y = 2 * x + 1 
# Create a line plot with x values on the x-axis and y values on y-axis 
plt.plot(x, y) 
# Display the plot to the user 
plt.show() 
