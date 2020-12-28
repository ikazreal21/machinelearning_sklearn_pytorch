import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("car.data")
X = data[["buying", "maint", "safety"]].values

y = data[["class"]]

# convertion of string to numbers

# X
le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = le.fit_transform(X[:, i])

# y
label_mapping = {"unacc": 0, "acc": 1, "good": 2, "vgood": 3}
y["class"] = y["class"].map(label_mapping)
y = np.array(y)

# create a model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights="uniform")
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)

knn.fit(X_train, y_train)
prediction = knn.predict(X_test)
score = accuracy_score(y_test, prediction)
print("Prediction: ", prediction)
print("Score: ", score)


print("------------------------------------------------------------------------------")
a = int(input("Enter a Value: "))
print("actual value: ", y[a])
print("prediction value", knn.predict(X)[a])
