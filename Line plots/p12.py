import matplotlib.pyplot as plt 
import numpy as np 
# Generate values for x-axis 
x = np.linspace(0, 2 * np.pi, 40)  # 40 points from 0 to 2π 
print (‘Value of x is:’, x) 
# Compute sine values 
y = np.sin(x) 
print (‘Value of y is:’, y) 
# Create the plot 
plt.plot(x, y, label='Sine Wave') 
# Add labels and title 
plt.xlabel('X-axis (radians)') 
plt.ylabel('Y-axis (amplitude)') 
plt.title('Sine Wave') 
plt.legend() 
# Display the plot 
plt.show()
