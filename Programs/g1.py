import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the points as NumPy arrays
x = np.array([1, 2, 6, 18])
y = np.array([3, 10, 12, 20])

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Diagram')

# Show the plot
plt.grid(True)
plt.show()

