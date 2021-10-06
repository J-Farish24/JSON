import json
from typing import Text
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

FILE = "eq_data_30_day_m1.json"

infile = open(FILE, "r")


eq_data = json.load(infile)

infile.close()

magnitudes, latitudes, longitudes, hover_texts = [], [], [], []
count = 0

eq_list = eq_data["features"]
for earthquake in eq_list:
    mag = earthquake["properties"]["mag"]
    longitude = earthquake["geometry"]["coordinates"][0]
    latitude = earthquake["geometry"]["coordinates"][1]
    place = earthquake["properties"]["title"]
    magnitudes.append(mag)
    latitudes.append(latitude)
    longitudes.append(longitude)
    hover_texts.append(place)


print(magnitudes[:5])
print(latitudes[:5])
print(longitudes[:5])

data = [
    {
        "type": "scattergeo",
        "lon": longitudes,
        "lat": latitudes,
        "text": hover_texts,
        "marker": {
            "size": [mag * 5 for mag in magnitudes],
            "color": magnitudes,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquake 30 Days")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="globalearthquake1day.html")
