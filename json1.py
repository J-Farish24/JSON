import json

FILE = "eq_data_1_day_m1.json"

infile = open(FILE, "r")


eq_data = json.load(infile)

infile.close()

magnitudes = []
latitudes = []
longitudes = []
count = 0

eq_list = eq_data["features"]
for earthquake in eq_list:
    mag = earthquake["properties"]["mag"]
    longitude = earthquake["geometry"]["coordinates"][0]
    latitude = earthquake["geometry"]["coordinates"][1]
    magnitudes.append(mag)
    latitudes.append(latitude)
    longitudes.append(longitude)


print(magnitudes)
print(latitudes)
print(longitudes)

# Magnitude Latitude Longitude
