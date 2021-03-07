# from sklearn.model_selection import train_test_split
from PIL import Image
import numpy as np
import mnist
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import joblib

# data manipulation
X_train = mnist.train_images()
y_train = mnist.train_labels()
X_test = mnist.test_images()
y_test = mnist.test_labels()
X_train = X_train.reshape((-1, 28 * 28))
X_test = X_test.reshape((-1, 28 * 28))
X_train = X_train / 256
X_test = X_test / 256


# Model, traing , prediction
clf = MLPClassifier(solver="adam", activation="relu",
                    hidden_layer_sizes=(64, 64))
# clf.fit(X_train, y_train)
# prediction = clf.predict(X_test)

# saving
filename = "model2_0.98acc.sav"
# joblib.dump(clf, filename)

model = joblib.load(filename)

prediction = model.predict(X_test)


acc = confusion_matrix(y_test, prediction)


def accuracy(confusion_matrix):
    diagonal = confusion_matrix.trace()
    elements = confusion_matrix.sum()
    return diagonal / elements


print("Accuracy :", accuracy(acc))


# image insert
img = Image.open("five2.png")
data = list(img.getdata())


for i in range(len(data)):
    data[i] = 255 - data[i]

pred = np.array(data) / 256
p = model.predict([pred])
print("Prediction: ", p)
