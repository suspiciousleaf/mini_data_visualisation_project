import plotly.express as px
import requests

# Download earthquake activity in last 30 days over M1.0
eq_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
contents = requests.get(eq_url)
all_eq_data = contents.json()

# Assign earthquakes list to variable for easier access
all_eq_dicts = all_eq_data["features"]


mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

title = all_eq_data["metadata"]["title"]
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
