import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the points as NumPy arrays
x_values = np.array([1, 2, 3, 4])
y_values = np.array([10, 20, 30, 40])

# Create a new figure and axis
fig, ax = plt.subplots()

# Display the grid
ax.grid(True)

# Create a line plot connecting the points
ax.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot with Grid')

# Show the plot
plt.show()

