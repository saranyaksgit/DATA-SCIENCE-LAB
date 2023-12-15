import matplotlib.pyplot as plt

with open('/home/student/Desktop/data.txt', 'r') as file:
    lines = file.readlines()

temperature = []
sales = []

for line in lines[1:]:
    data = line.strip().split(',')

    temperature.append(int(data[0]))
    sales.append(float(data[1]))  

plt.plot(temperature, sales, marker='o', linestyle='-', color='b')
plt.xlabel('Temperature in degree Celsius')
plt.ylabel('Sales')
plt.title('Sales vs Temperature')
plt.grid(True)
plt.show()

