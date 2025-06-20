import matplotlib.pyplot as plt
# Example data: Ages of a group of people 
data = [18, 20, 22, 21, 24, 30, 28, 27, 33, 35, 38, 40, 42, 45] 
# Create a histogram 
plt.hist(data, bins=5, edgecolor='black', color='skyblue') 
# Add labels and title 
plt.xlabel('Age') 
plt.ylabel('Frequency') 
plt.title('Age Distribution') 
# Show the histogram 
plt.show() 
#Explanation: 
#• data: The dataset to be plotted as a histogram. 
#• plt.hist(): Creates the histogram. 
#o bins=5: Specifies the number of bins (intervals) to use. 
#o edgecolor='black': Adds a black border to each bar in the histogram. 
#o color='skyblue': Sets the color of the bars to sky blue. 
#• plt.xlabel(): Sets the label for the x-axis. 
#• plt.ylabel(): Sets the label for the y-axis. 
#• plt.title(): Sets the title of the histogram. 
#• plt.show(): Displays the histogram.
