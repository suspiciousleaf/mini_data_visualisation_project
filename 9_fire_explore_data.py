import csv
import plotly.express as px

#! Convert to CSV and make the graph work

# Read data as a string and convert to a Python object.
with open("eq_data/world_fires_1_day.geojson", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

reader = csv.reader(lines)
header_row = next(reader)


# Assign earthquakes list to variable for easier access
all_eq_dicts = all_fire_data["features"]


mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

title = all_fire_data["metadata"]["title"]
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="agsunset",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
