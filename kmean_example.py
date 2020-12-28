from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
import pandas as pd


bc = load_breast_cancer()

X = scale(bc.data)
y = bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)


mod = KMeans(n_clusters=2, random_state=0)
mod.fit(X_train)
prediction = mod.predict(X_test)
label = mod.labels_

print("Labels: ", label)
print("Accutal: ", y_test)
print("Prediction:", prediction)
print("Accuracy:", accuracy_score(y_test, prediction))

print(pd.crosstab(y_train, label))