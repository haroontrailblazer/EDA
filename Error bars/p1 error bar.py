import matplotlib.pyplot as plt 
import numpy as np 
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 3, 5, 7, 11]) 
yerr = np.array([0.5, 0.2, 0.3, 0.4, 0.6]) 
plt.errorbar(x, y, yerr=yerr, fmt='o', ecolor='red', 
elinewidth=2, capsize=5) 
plt.xlabel('X-axis Label') 
plt.ylabel('Y-axis Label') 
plt.title('Plot with Vertical Error Bars') 
plt.show()