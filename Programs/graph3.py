import matplotlib.pyplot as plt

x = [1, 2, 6]
y = [3, 10, 12]

plt.plot(x, y, marker='o')

plt.scatter(x, y, color='red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Diagram')


plt.xlim(0, 7)
plt.ylim(0, 15)

plt.show()
