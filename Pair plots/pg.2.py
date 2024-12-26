import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Pair plot with different markers
plt.figure(figsize=(16, 9), dpi=900)
sns.pairplot(df, hue='species', markers=["o", "s", "D"])
plt.title('Pair Plot with Different Markers')
plt.show()