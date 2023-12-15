import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the points as NumPy arrays
x_values = np.array([1, 2, 6])
y_values = np.array([3, 10, 12])

# Create a line plot with marked points
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Marked Points')

# Show the plot
plt.grid(True)
plt.show()

