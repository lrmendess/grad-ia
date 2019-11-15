def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

col = lambda arr, index_collection: [[a[index] for index in index_collection] for a in arr]

def sfs():
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(x_train, y_train)

    # print(knn.score(x_test, y_test))

    for i in range(len(x_train[0])):
        pass

sfs()

