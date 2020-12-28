import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split

# from sklearn.metrics import accuracy_score

boston = datasets.load_boston()


boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df["Price"] = boston.target
X = boston_df
y = boston.target
# Bar graph
# plt.figure(figsize=(12, 6))
# sns.set("notebook")
# sns.displot(boston_df.Price, bins=20)
# plt.show()

# Reg
# for i in X.columns:
#     plt.scatter(X[i], y)
#     plt.xlabel(i)
#     plt.ylabel("Price")
#     plt.show()


# heatmap
plt.figure(figsize=(12, 6))
val = boston_df.corr()
sns.heatmap(data=val, annot=True)
plt.show()


# print(boston_df.head())
# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)
