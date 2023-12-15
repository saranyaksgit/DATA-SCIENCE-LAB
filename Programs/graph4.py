import matplotlib.pyplot as plt

x = [1, 3, 6, 18]
y = [6, 8, 12, 20]

plt.plot(x, y, color='red', linestyle='dotted')
plt.scatter(x, y, color='green')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Diagram')

plt.show()
