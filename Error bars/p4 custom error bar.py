import matplotlib.pyplot as plt 
import numpy as np 
x = np.array([1, 2, 3, 4, 5]) 
y = np.array([2, 3, 5, 7, 11]) 
def custom_error(x): 
	return 0.1 * x 
yerr = custom_error(x) 
plt.errorbar(x, y, yerr=yerr, fmt='o', ecolor='purple', 
elinewidth=1, capsize=3) 
plt.xlabel('X-axis Label') 
plt.ylabel('Y-axis Label') 
plt.title('Plot with Custom Error Bars') 
plt.show()