import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Basic pair plot
sns.pairplot(df, hue='species')
plt.title('Basic Pair Plot')
plt.figure(figsize=(16,9),dpi=900)
plt.show()