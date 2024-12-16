import matplotlib.pyplot as plt 
import matplotlib.patches as patches 
# Example data 
x = [1, 2, 3, 4, 5] 
y1 = [2, 3, 5, 7, 11] 
y2 = [1, 4, 6, 8, 10] 
# Create line plots 
plt.plot(x, y1, color='blue', marker='o')  # Data series 1 
plt.plot(x, y2, color='red', linestyle='--')  # Data series 2 
# Create custom legend handles with color boxes 
legend_handles = [ 
patches.Patch(color='blue', label='Series 1'),  # Blue color box for Series 1 
patches.Patch(color='red', label='Series 2')    # Red color box for Series 2 
] 
# Add the legend with custom handles 
plt.legend(handles=legend_handles, loc='upper left') 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis')
plt.title('Line Plot with Color Box Legend') 
# Show the plot 
plt.show()
