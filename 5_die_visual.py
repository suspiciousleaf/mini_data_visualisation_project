import plotly.express as px
from die import Die

# Create a Die instance
die = Die()

# Choose how many dice to roll at once
num_dice = 4


# Make some rolls, and store results in a list.
rolls = 100000
results = [sum([die.roll() for _ in range(num_dice)]) for _ in range(rolls)]


# Analyze the results.

max_result = num_dice * die.num_sides
poss_results = range(num_dice, max_result + 1)

frequencies = [results.count(value) for value in poss_results]


# Visualize the results.
title = f"Results of Rolling {num_dice} D{die.num_sides} {rolls} Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html("5_die_visual.html")
