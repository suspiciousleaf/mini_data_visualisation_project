from pathlib import Path
import json

# Read data as a string and convert to a Python object.
# path = Path("eq_data/eq_data_1_day_m1.geojson")
# contents = path.read_text()

with open("eq_data/eq_data_1_day_m1.geojson", "r", encoding="utf-8") as infile:
    contents = infile.read()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))
print(all_eq_dicts[0])
