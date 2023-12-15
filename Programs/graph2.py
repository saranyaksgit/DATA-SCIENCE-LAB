import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 14, 16, 18, 20])  
y = np.array([3, 10, 12, 16, 20])  

plt.xlabel('Time')
plt.ylabel('Speed')
plt.title('Time-Speed Diagram')
plt.plot(x, y)  
plt.show()
