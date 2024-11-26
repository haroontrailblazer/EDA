import matplotlib.pyplot as plt 
# Example data 
x = [1, 2, 3, 4, 5] 
y1 = [2, 3, 5, 7, 11] 
y2 = [1, 4, 6, 8, 10] 
# Create line plots 
line1, = plt.plot(x, y1, color='blue', marker='o') 
line2, = plt.plot(x, y2, color='red', linestyle='--') 
# Add a customized legend 
plt.legend([line1, line2], ['Series 1', 'Series 2'], 
loc='upper left', title='Data Series', fontsize='small', 
frameon=False) 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Line Plot with Customized Legend') 
# Show the plot 
plt.show() 
