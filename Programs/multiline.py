import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temp_cityA = [10, 12, 15, 18, 22, 25, 28, 27, 24, 20, 15, 12]
temp_cityB = [8, 11, 14, 18, 22, 26, 30, 29, 26, 21, 16, 11]

plt.plot(months, temp_cityA, label='City A', marker='o', linestyle='-', color='b')

plt.plot(months, temp_cityB, label='City B', marker='s', linestyle='--', color='r')

plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Changes for City A and City B')

plt.legend()

plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()

