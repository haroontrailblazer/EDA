import matplotlib.pyplot as plt 
# Sample data 
x = [1, 2, 3, 4, 5] 
y = [2, 3, 5, 7, 11] 
# Create a figure 
plt.figure(figsize=(10, 6), dpi=80) 
# Plot with customizations 
plt.plot(x, y, color='blue', linestyle='-', 
marker='o', markersize=8, linewidth=2, 
label='Data Line') 
# Add a title and labels 
plt.title('Customized Plot', fontsize=14, fontweight='bold', color='darkblue') 
plt.xlabel('X-axis', fontsize=12, color='green') 
plt.ylabel('Y-axis', fontsize=12, color='red') 
# Customize grid lines 
plt.grid(True, linestyle='--', color='gray', linewidth=0.5) 
# Customize ticks 
plt.tick_params(axis='both', which='major', labelsize=10, length=6, width=2, direction='in') 
# Add legend
plt.legend(loc='upper left', fontsize=10, frameon=False, title='Legend Title') 
# Customize plot borders 
plt.gca().spines['top'].set_color('blue') 
plt.gca().spines['top'].set_linewidth(1.5) 
# Annotate a point 
plt.annotate('Important Point', xy=(3, 5), xytext=(4, 6), 
arrowprops=dict(facecolor='black', arrowstyle='->'), 
fontsize=12, color='purple') 
# Show the plot 
plt.tight_layout() 
plt.show() 
