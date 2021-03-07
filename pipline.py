from sklearn import datasets
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.5)
