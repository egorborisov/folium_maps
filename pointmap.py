import pandas as pd
import folium
from folium.plugins import MarkerCluster

# load data (the data is not available here due to confidentiality reasons)
df = pd.read_csv('data.csv')

# map initialization
cmap = folium.Map(location=[59.95525, 30.2923], zoom_start=13)

# marker layer
mc = MarkerCluster()

# add markers
for i, row in df.iterrows():
    mc.add_child(folium.Marker(location=[row.lat, row.lng]))

# put all together
cmap.add_child(mc)

# save map as web page
cmap.save("marker_map.html")
