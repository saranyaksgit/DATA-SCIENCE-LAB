import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, ax = plt.subplots()
ax.set_xticks(range(11))
ax.set_yticks(range(11))
ax.grid(True)

plt.plot(x, y, marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart')

plt.show()
