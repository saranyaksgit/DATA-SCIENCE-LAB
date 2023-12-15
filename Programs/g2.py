import numpy as np
import matplotlib.pyplot as plt

# Define the data points as NumPy arrays
x_values = np.array([2, 14, 16, 18, 20])
y_values = np.array([100, 200, 250, 400, 300])

# Create a line plot
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot Example')

# Show the plot
plt.grid(True)
plt.show()

