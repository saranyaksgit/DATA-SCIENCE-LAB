import seaborn as sns 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
    
sizes = [100, 200, 300, 400, 500]
sns.scatterplot(x=x, y=y, size=sizes, sizes=(100, 500))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bubble Plot')

plt.show()

