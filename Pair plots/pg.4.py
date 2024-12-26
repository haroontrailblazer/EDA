import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Pair plot with regression lines
plt.figure(figsize=(16, 9), dpi=900)
sns.pairplot(df, hue='species', kind='reg')
plt.title('Pair Plot with Regression Lines')
plt.show()