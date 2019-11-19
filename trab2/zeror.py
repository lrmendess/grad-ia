def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin

from collections import Counter

class ZeroR(BaseEstimator, ClassifierMixin):
    def __init__(self):
        self.class_ = 0

    def fit(self, x_train, y_train):
        group_by = Counter(y_train)
        self.class_ = max(group_by.items(), key=lambda x: x[1])[0]

    def predict(self, x_test):
        return [self.class_] * len(x_test)

if __name__ == '__main__':
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

    zr = ZeroR()
    zr.fit(x_train, y_train)

    predict = zr.predict(x_test)
    accuracy = zr.score(x_test, y_test)

    print(f"Predict: {predict}")
    print(f"Accuracy: {accuracy}")