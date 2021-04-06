# import folium package
import folium

# Map method of folium return Map object

# Here we pass coordinates of Gfg
# and starting Zoom level = 12
my_map1 = folium.Map(location=[28.5011226, 77.4099794],
                     zoom_start=12)

# save method of Map object will create a map
my_map1.save("my_map1.html")