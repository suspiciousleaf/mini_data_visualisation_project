import matplotlib.pyplot as plt

input_values = [num for num in range(1, 1001)]
squares = [x**2 for x in input_values]

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.savefig("2_scatter_graph_squares.png", bbox_inches="tight")
plt.show()
