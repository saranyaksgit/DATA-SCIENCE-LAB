import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the points as NumPy arrays
x_values = np.array([1, 3, 6, 18])
y_values = np.array([6, 8, 12, 20])

# Create a color gradient from green to red
colors = np.linspace(0, 1, len(x_values)-1)

# Create a line plot with varying colors and a dotted line style
for i in range(len(x_values) - 1):
    plt.plot(x_values[i:i+2], y_values[i:i+2], linestyle='dotted', color=plt.cm.RdYlGn(colors[i]), marker='o', markersize=8, label=f'Point {i+1}-{i+2}')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Varying Colors and Dotted Line')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

