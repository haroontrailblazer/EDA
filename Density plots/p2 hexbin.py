import matplotlib.pyplot as plt 
import numpy as np 
# Generate random data 
x = np.random.randn(1000) 
y = np.random.randn(1000) 
# Create a hexagonal binning density plot 
plt.hexbin(x, y, gridsize=30, cmap='Blues')
# Add colorbar to show the density scale 
plt.colorbar(label='Density')
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Hexbin Density Plot') 
# Show plot 
plt.show()
