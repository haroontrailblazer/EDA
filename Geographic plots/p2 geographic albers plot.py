from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt 
# Create a map using the Albers projection 
m = Basemap(projection='aea',  
llcrnrlat=20, urcrnrlat=60,  # Latitude range 
llcrnrlon=-130, urcrnrlon=-60,  # Longitude range 
lat_1=20, lat_2=40,  # Standard parallels 
lon_0=-100,  # Central longitude 
resolution='c') 
# Draw map boundaries and features 
m.drawcoastlines()
m.drawcountries()
m.drawstates()
                # Draw coastlines 
                 # Draw country borders 
                    # Draw US state boundaries 
m.fillcontinents(color='lightgreen', lake_color='aqua')  # Fill continents with color 
m.drawmapboundary(fill_color='aqua')  # Draw boundary and fill oceans with color 
# Draw parallels (latitude) and meridians (longitude) 
m.drawparallels(range(20, 61, 10), labels=[1,0,0,0])  # Label parallels on the left side 
m.drawmeridians(range(-130, -59, 10), labels=[0,0,0,1])  # Label meridians on the bottom 
# Show the map 
plt.title("Simple Albers Equal-Area Projection") 
plt.show()