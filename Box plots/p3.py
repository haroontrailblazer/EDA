import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating random data
np.random.seed(10)
df = pd.DataFrame({
    'A': np.random.normal(0, 1, 100),
    'B': np.random.normal(1, 2, 100),
    'C': np.random.normal(2, 3, 100)
})

# Creating a box plot
df.boxplot()
plt.title('Box plot for multiple columns using Pandas')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
