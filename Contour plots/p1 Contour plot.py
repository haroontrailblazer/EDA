import matplotlib.pyplot as plt 
import numpy as np 
# Create a grid of x and y values 
x = np.linspace(-5, 5, 100) 
y = np.linspace(-5, 5, 100) 
X, Y = np.meshgrid(x, y) 
# Define a function Z = f(X, Y) 
Z = np.sin(np.sqrt(X**2 + Y**2)) 
# Create contour plot 
plt.contour(X, Y, Z, levels=10, cmap='viridis') 
plt.colorbar(label='Z value') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Contour Plot')  
plt.show()
#• matplotlib.pyplot is used for creating plots. 
#• numpy is used for numerical operations and generating arrays. 
#• x and y are arrays of 100 linearly spaced values from -5 to 5. 
#• np.meshgrid(x, y) creates 2D grids of x and y values, which will be used to compute the function values over a grid. 
#• Z is computed as sin(sqrt(X^2 + Y^2)), which generates a 2D array representing the values of the function at each grid point (X, Y). 
#• plt.contour(X, Y, Z): Creates contour lines for the function Z. 
#• levels=10: Specifies that 10 contour levels should be drawn. 
#• cmap='viridis': Applies the 'viridis' colormap to the contours, which maps the contour levels to colors. 
#• plt.colorbar(label='Z value'): Adds a colorbar to the plot, which indicates the mapping of colors to Z values. 
#• plt.xlabel('X-axis') and plt.ylabel('Y-axis'): Add labels to the x-axis and y-axis. 
#• plt.title('Contour Plot'): Adds a title to the plot. 
#• plt.show() renders and displays the plot. 
