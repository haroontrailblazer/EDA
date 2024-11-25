import geopandas as gpd
import matplotlib.pyplot as plt

# Path to the downloaded shapefile (update the path accordingly)
shapefile_path = r'C:\countries\ne_110m_admin_0_countries.shp'

# Load the shapefile using GeoPandas
world = gpd.read_file(shapefile_path)

# Plot the world map
world.plot(figsize=(10, 6), color='lightblue', edgecolor='black')

# Add a title
plt.title('World Map', fontsize=16)

# Show the plot
plt.show()