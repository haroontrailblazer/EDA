import matplotlib.pyplot as plt 
# Data 
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
B = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21] 
C = [5, 9, 13, 16, 21, 13, 9, 20, 21, 11] 
# Create scatter plots for the three variables 
plt.scatter(A, B, color='blue', label='Value of A vs. B', marker='o') 
plt.scatter(A, C, color='red', label='Value A vs. C', marker='x') 
# Add labels and title 
plt.xlabel('Value A') 
plt.ylabel('Values') 
plt.title('Scatter Plot of Three Variables') 
plt.legend() 
# Display the plot 
plt.show()
