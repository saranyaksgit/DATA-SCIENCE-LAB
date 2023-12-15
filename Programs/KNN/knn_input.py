from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn import metrics

# Load the Iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# Prompt the user to input values for a sample
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

sample = [[sepal_length, sepal_width, petal_length, petal_width]]

# Train the K-nearest neighbors classifier
c_knn = KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x, y)

# Predict the class of the user-input sample
pred = c_knn.predict(sample)
pred_v = [iris.target_names[p] for p in pred]
print("Predicted class: ", pred_v[0])

