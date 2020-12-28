import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

dt = pd.read_csv("music.csv")
X = dt.drop(columns=["genre"])
y = dt["genre"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)
mod = DecisionTreeClassifier()
mod.fit(X, y)
tree.export_graphviz(
    mod,
    out_file="mrec.dot",
    feature_names=["age", "gender"],
    class_names=sorted(y.unique()),
    label=all,
    rounded=True,
    filled=True,
)


# prediction = mod.predict(X_test)
# score = accuracy_score(y_test, prediction)
# print(score)