import matplotlib.pyplot as plt 
# Create a figure 
plt.figure(figsize=(10, 6)) 
# First subplot (2x2 grid, 1st subplot) 
plt.subplot(2, 2, 1) 
plt.plot([1, 2, 3], [4, 5, 6], 'r-o') 
plt.title('Plot 1') 
# Second subplot (2x2 grid, 2nd subplot) 
plt.subplot(2, 2, 2) 
plt.scatter([1, 2, 3], [4, 5, 6], c='b', marker='s') 
plt.title('Plot 2') 
# Third subplot (2x2 grid, 3rd subplot) 
plt.subplot(2, 2, 3) 
plt.bar([1, 2, 3], [4, 5, 6], color='g') 
plt.title('Plot 3') 
# Fourth subplot (2x2 grid, 4th subplot) 
plt.subplot(2, 2, 4) 
plt.hist([1, 2, 1, 2, 3, 3, 3], bins=3, color='y') 
plt.title('Plot 4') 
# Adjust layout 
plt.tight_layout() 
# Show the figure 
plt.show()
