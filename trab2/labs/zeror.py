def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

from sklearn import datasets
from sklearn.model_selection import train_test_split

from collections import Counter

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

class ZeroR():
    def __init__(self):
        self.class_ = 0

    def fit(self, x_train, y_train):
        group_by = Counter(y_train)
        self.class_ = max(group_by.items(), key=lambda x: x[1])[0]

    def predict(self, x_test, y_test):
        return [self.class_] * len(y_test)

zr = ZeroR()
zr.fit(x_train, y_train)

equals = zip(zr.predict(x_test, y_test), y_test)
equals = filter(lambda x: x[0] == x[1], equals)

print(len(list(equals)) / len(list(y_test)))
