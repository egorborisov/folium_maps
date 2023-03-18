import pandas as pd
from folium.plugins import HeatMap
import folium

# load data (the data is not available here due to confidentiality reasons)
df = pd.read_csv('people.csv')
branches = pd.read_csv('branches.csv')
competitor = pd.read_csv('competitors.csv')

# map initialization
hmap = folium.Map(location=[59.95, 30.15], zoom_start=11)

# layer with people count
people = folium.FeatureGroup(name='People count')

hm = HeatMap(
    list(zip(df['lat'], df['lng'], df['people'])),
    min_opacity=.1,
    max_val=df['people'].max(),
    radius=15,
    blur=25,
    max_zoom=1,
)

people.add_child(hm)

# own branches amd competitors
filial_markers = folium.FeatureGroup(name='Branches')

for i, row in branches.iterrows():
    folium.Marker(
        location=[row['lat'], row['lng']],
        popup=row['name'],
        icon=folium.Icon(color='blue', icon='cloud')
    ).add_to(filial_markers)

# competitors
competitor_markers = folium.FeatureGroup(name='Competitors')

for index, row in competitor.iterrows():
    folium.Marker(
        location=[row['lat'], row['lng']],
        popup=row['name'],
        icon=folium.Icon(color='red')
    ).add_to(competitor_markers)

# put all together
hmap.add_child(people)
hmap.add_child(filial_markers)
hmap.add_child(competitor_markers)

# layer control
folium.LayerControl(collapsed=False).add_to(hmap)

# save map as a web page
hmap.save('people_spb.html')
