import geopandas as gpd
import matplotlib.pyplot as mp
fp=input(r"Enter your file path")
fig = gpd.read_file(fp)
fig.plot(figsize=(10, 6), color='lightblue', edgecolor='black')
plt.title(fp, fontsize=16)
plt.show()
