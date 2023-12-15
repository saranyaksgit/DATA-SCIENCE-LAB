import matplotlib.pyplot as plt

class_names = ['Class A', 'Class B', 'Class C']
test_scores = {
    'Class A': [85, 90, 88, 78, 92, 85, 89],
    'Class B': [75, 80, 82, 70, 78, 75, 80],
    'Class C': [92, 88, 90, 85, 95, 88, 92]
}

data = [test_scores[class_name] for class_name in class_names]

plt.boxplot(data, labels=class_names, vert=False, patch_artist=True)

plt.xlabel('Test Scores')
plt.title('Distribution of Test Scores for Different Classes')

plt.show()

