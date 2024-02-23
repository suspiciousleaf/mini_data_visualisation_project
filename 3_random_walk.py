from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Decide which direction to go, and how far to go.
        return choice([1, -1]) * choice([0, 1, 2, 3, 4])

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)


fig, ax = plt.subplots(figsize=(12, 6), dpi=102)

num_walks = 1
for _ in range(num_walks):
    rw = RandomWalk(100_000)
    rw.fill_walk()
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )
    # Emphasize the first and last points.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

# Create line graph of random walk
# rw = RandomWalk(5_000)
# rw.fill_walk()
# point_numbers = range(rw.num_points)
# ax.plot(
#     rw.x_values,
#     rw.y_values,
#     linewidth=1,
# )


# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.style.use("classic")

ax.set_title("Random Walk", fontsize=24)


# Set size of tick labels
ax.tick_params(labelsize=14)

ax.set_aspect("equal")

plt.savefig("3_random_walk.png", bbox_inches="tight")
plt.show()
