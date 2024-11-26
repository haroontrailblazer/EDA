import matplotlib.pyplot as plt 
# Create sample data 
x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11] 
# Create a plot 
plt.plot(x, y, 'bo-', label='Data Points') 
# Add text to the plot 
plt.text(3, 7, 'This is a key point', fontsize=12, color='green', 
ha='center') 
# Add a basic annotation with an arrow 
plt.annotate('Highest Point', xy=(5, 11), xytext=(4, 12), 
arrowprops=dict(facecolor='red', shrink=0.05)) 
# Add labels and title 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.title('Plot with Text and Annotation') 
plt.legend() 
# Show the plot 
plt.show()
