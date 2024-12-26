import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Pair plot with KDE diagonal
plt.figure(figsize=(16, 9), dpi=900)
sns.pairplot(df, hue='species', diag_kind='kde')
plt.title('Pair Plot with KDE Diagonal')
plt.show()