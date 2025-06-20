import matplotlib.pyplot as plt 
import numpy as np 
# Spiral controls the number of Spiral 
spiral = 5 
# data 
zline = np.linspace(0,5,100) 
xline = np.cos(spiral * zline) 
yline = np.sin(spiral * zline) 
ax = plt.axes(projection ='3d') 
ax.plot3D(xline, yline, zline, lw=5); 
ax.set_xlabel('X - Axis') 
ax.set_ylabel('Y - Axis') 
ax.set_zlabel('Z - Axis') 
plt.show()