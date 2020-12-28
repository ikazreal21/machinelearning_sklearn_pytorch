import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import neighbors, datasets
from mlxtend.plotting import plot_decision_regions
from sklearn.preprocessing import LabelEncoder


def knvis(data, k):
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

    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(X, y)

    # Plotting decission regions
    plot_decision_regions(X, y, clf=clf, legend=2)

    # axes annotations
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Kn Vis")
    plt.show()


knn = pd.read_csv("car.data")

for i in [1, 5, 20, 30, 40, 80]:
    knvis(knn, i)