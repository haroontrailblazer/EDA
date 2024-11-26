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
#• plt.contourf(X, Y, Z) generates a filled contour plot. 
#• levels=10 specifies that the plot should display 10 levels of contours. 
#• cmap='viridis' applies the 'viridis' colormap to the filled contours, providing a color gradient based on Z values. 
#• plt.colorbar(label='Z value') adds a colorbar to indicate the mapping of colors to Z values. 
#• plt.xlabel('X-axis') and plt.ylabel('Y-axis') label the x-axis and y-axis. 
#• plt.title('Filled Contour Plot') sets the title of the plot. 
#• plt.show() renders and displays the plot. 
