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
