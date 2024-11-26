import matplotlib.pyplot as plt 
# Create a grid of 2x2 subplots 
fig, axs = plt.subplots(2, 2, figsize=(10, 6)) 
# First subplot 
axs[0, 0].plot([1, 2, 3], [4, 5, 6], 'r-o') 
axs[0, 0].set_title('Plot 1') 
# Second subplot 
axs[0, 1].scatter([1, 2, 3], [4, 5, 6], c='b', marker='s') 
axs[0, 1].set_title('Plot 2') 
# Third subplot 
axs[1, 0].bar([1, 2, 3], [4, 5, 6], color='g') 
axs[1, 0].set_title('Plot 3') 
# Fourth subplot 
axs[1, 1].hist([1, 2, 1, 2, 3, 3, 3], bins=3, color='y') 
axs[1, 1].set_title('Plot 4') 
# Adjust layout 
plt.tight_layout() 
# Show the figure 
plt.show()
