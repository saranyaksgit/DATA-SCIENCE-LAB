import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [50, 55, 60, 70, 75, 80, 85, 90]

plt.scatter(hours_studied, test_scores, label='Test Scores', color='b', marker='o')

plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.title('Relationship between Hours Studied and Test Scores')

plt.legend()

plt.show()

