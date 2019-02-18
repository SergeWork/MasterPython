import folium
from folium.plugins import MarkerCluster
import pandas as pd


def color_change(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(tiles="Mapbox bright", location=[37.296933,-121.9574983], zoom_start=5)
cluster = MarkerCluster().add_to(map)

data = pd.read_csv("data/volcanoes_USA.txt")

lat = data['LAT']
lon = data['LON']
name = data['NAME']
elev = data['ELEV']

for lat, lon, name, elev in zip(lat, lon, name, elev):
    folium.Marker(location=[lat, lon], popup=name + ": " + str(elev), icon=folium.Icon(color=color_change(elev))).add_to(cluster)

map.save("map1.html")
