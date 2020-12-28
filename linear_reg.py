from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sns

# from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt


boston = datasets.load_boston()
X = boston.data
y = boston.target

# print("X")
# print(X)
# print(X.shape)
# print("y")
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)

# algo / model
li_reg = linear_model.LinearRegression()

# visualize the data
# plt.scatter(X.T[5], y)
# plt.scatter(X.T[3], y)
# plt.scatter(X.T[7], y)
# plt.show()

model = li_reg.fit(X_train, y_train)
prediction = model.predict(X_test)
# accuracy = accuracy_score(y_test, prediction)
print("Prediction: ", prediction)
print("R^2: ", li_reg.score(X, y))
print("coef: ", li_reg.coef_)
# print("Accuracy: ", accuracy)
print("Intercept: ", li_reg.intercept_)


# a = int(input("Enter a Number to Predict: "))
# print("Prediction: ", model.predict(X)[a])
# print("Accutal Value: ", y[a])
