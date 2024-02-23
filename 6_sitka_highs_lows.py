from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


def convert_f_to_c(temp_f):
    return (5 / 9) * (int(temp_f) - 32)


# Extract dates and temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = convert_f_to_c(row[4])
    low = convert_f_to_c(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high temperatures
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Format plot
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
