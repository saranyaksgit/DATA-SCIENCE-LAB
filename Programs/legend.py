import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5]
y1 =[2, 4, 6, 8,10]
y2 =[3, 6, 9, 12, 15]

plt.plot(x, y1, label='line 1')
plt.plot(x, y2, label='line 2')

plt.legend()

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines Plot')

plt.show()
