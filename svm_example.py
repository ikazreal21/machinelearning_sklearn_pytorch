from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm


iris = datasets.load_iris()

X = iris.data
y = iris.target

classes = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

model = svm.SVC()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
acc = accuracy_score(y_test, prediction)
print("Acctual:    ", y_test)
print("Prediction: ", prediction)
print("Accuracy: ", acc)