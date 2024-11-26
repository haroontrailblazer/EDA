import matplotlib.pyplot as plt 
import numpy as np 
# Create a grid of x and y values 
x = np.linspace(-5, 5, 100) 
y = np.linspace(-5, 5, 100) 
X, Y = np.meshgrid(x, y) 
# Define a function Z = f(X, Y) 
Z = np.sin(np.sqrt(X**2 + Y**2)) 
# Create filled contour plot 
plt.contourf(X, Y, Z, levels=10, cmap='viridis') 
plt.colorbar(label='Z value') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Filled Contour Plot')  
plt.show()
#• matplotlib.pyplot is used for creating and displaying plots. 
#• numpy is used for numerical operations and generating arrays. 
#• x and y are arrays of 100 linearly spaced values ranging from -5 to 5. 
#• np.meshgrid(x, y) creates 2D grids X and Y from these arrays. These grids represent the x and y coordinates for each point in the plot. 
#• Z is calculated as the sine of the square root of the sum of squares of X and Y. This represents the function values over the grid.
