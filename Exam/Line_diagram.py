import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,6,18])
y = np.array([3,10,12,20])
plt.title("Line diagram")
plt.xlabel("x axis ")
plt.ylabel("y axis")
plt.plot(x, y, color ="red",linestyle="dotted",marker="o",mfc="green",mec="green")
plt.show()
