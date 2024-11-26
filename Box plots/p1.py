import matplotlib.pyplot as plt
import numpy as np

# Generating random data
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Creating a box plot
plt.boxplot(data)
plt.title('Box plot using Matplotlib')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
