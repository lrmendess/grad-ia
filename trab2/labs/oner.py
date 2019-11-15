def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import pandas as pd

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels

class OneR():
    def fit(self, x_train, y_train):
        self.class_  = unique_labels(y_train)
        self.x_train = x_train
        self.y_train = y_train

        bins = [len(self.class_)] * len(self.x_train[0])
        bins = preprocessing.KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy='uniform').fit(self.x_train).transform(self.x_train)

        iterations = len(self.x_train[0])
        
        for i in range(iterations):
            cross = pd.crosstab(bins[:,i], self.y_train)
            print(cross)

    def predict(self, x_test, y_test):
        return None

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

oner = OneR()
oner.fit(x_train, y_train)
