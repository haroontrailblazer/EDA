from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt 
# Create a simple map using the Mercator projection 
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=60, 
llcrnrlon=-180, urcrnrlon=180, resolution='c') 
# Draw map boundaries and features 
m.drawcoastlines()
 m.drawcountries()
                # Draw coastlines 
                 # Draw country borders 
m.fillcontinents(color='lightgreen', lake_color='aqua')  # Fill continents with color 
m.drawmapboundary(fill_color='aqua')  # Draw boundary and fill oceans with color 
# Draw parallels (latitude) and meridians (longitude) 
m.drawparallels(range(-90, 90, 30), labels=[1,0,0,0])  # Label parallels on the left side 
m.drawmeridians(range(-180, 180, 60), labels=[0,0,0,1])  # Label meridians on the bottom 
# Show the map 
plt.title("Simple Mercator Projection") 
plt.show() 
P43. Robinson Projection 
from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt 
# Create a simple map using the Robinson projection 
m = Basemap(projection='robin', lon_0=0, resolution='c')
# Draw map boundaries and features 
m.drawcoastlines()
 m.drawcountries()
                # Draw coastlines 
                 # Draw country borders 
m.fillcontinents(color='lightgreen', lake_color='aqua')  # Fill continents with color 
m.drawmapboundary(fill_color='aqua')  # Draw boundary and fill oceans with color 
# Draw parallels (latitude) and meridians (longitude) 
m.drawparallels(range(-90, 90, 30), labels=[1,0,0,0])  # Label parallels on the left side 
m.drawmeridians(range(-180, 180, 60), labels=[0,0,0,1])  # Label meridians on the bottom 
# Show the map 
plt.title("Simple Robinson Projection") 
plt.show() 
