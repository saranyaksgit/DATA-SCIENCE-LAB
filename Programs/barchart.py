import matplotlib.pyplot as plt
import numpy as np

x = ['Maths', 'Physics', 'Chemistry', 'Biology']
y = [30, 40, 15, 25]

plt.barh(x, y)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Marksheet')

plt.show()

