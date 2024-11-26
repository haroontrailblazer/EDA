import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generating random data
np.random.seed(10)
data = pd.DataFrame({
    'Category': np.repeat(['A', 'B', 'C'], 100),
    'Values': np.concatenate([np.random.normal(loc, 1, 100) for loc in range(3)])
})

# Creating a box plot
sns.boxplot(x='Category', y='Values', data=data)
plt.title('Box plot using Seaborn')
plt.show()
