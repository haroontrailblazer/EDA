import matplotlib.pyplot as plt 
import numpy as np 
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 3, 5, 7, 11]) 
xerr = np.array([0.1, 0.2, 0.1, 0.3, 0.2]) 
plt.errorbar(x, y, xerr=xerr, fmt='o', ecolor='blue', elinewidth=1) 
plt.xlabel('X-axis Label') 
plt.ylabel('Y-axis Label') 
plt.title('Plot with Horizontal Error Bars')  
plt.show()
