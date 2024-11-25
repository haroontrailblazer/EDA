import matplotlib.pyplot as plt 
import numpy as np 
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 3, 5, 7, 11]) 
yerr = (np.array([0.2, 0.3, 0.1, 0.2, 0.4]), np.array([0.5, 0.4, 0.3, 0.4, 
0.6])) 
plt.errorbar(x, y, yerr=yerr, fmt='o', ecolor='green', elinewidth=2, 
capsize=4) 
plt.xlabel('X-axis Label') 
plt.ylabel('Y-axis Label') 
plt.title('Plot with Asymmetric Error Bars') 
plt.show()
