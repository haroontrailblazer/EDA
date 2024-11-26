import matplotlib.pyplot as plt 
# Example data 
x = [1, 2, 3, 4, 5] 
y1 = [2, 3, 5, 7, 11] 
y2 = [1, 4, 6, 8, 10] 
# Create a line plot 
plt.plot(x, y1, label='Series 1', color='blue', marker='o') 
plt.plot(x, y2, label='Series 2', color='red', linestyle='--') 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Line Plot with Legend') 
# Add a legend 
plt.legend() 
# Show the plot 
plt.show() 
