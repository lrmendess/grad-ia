def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

datasets = {
    'iris': datasets.load_iris(),
    'digits': datasets.load_digits(),
    'wine': datasets.load_wine(),
    'breast_cancer': datasets.load_breast_cancer()
}

classifiers = {
    'knn': KNeighborsClassifier(),
    'tree': DecisionTreeClassifier(),
    'neural': MLPClassifier(),
    'forest': RandomForestClassifier()
}

params = {
    'knn': {'n_neighbors': [1, 3, 5, 7, 10, 20]},
    'tree': {'max_depth': [None, 3, 5, 10]},
    'neural': {'max_iter': [50, 100, 200], 'hidden_layer_sizes': [(15,)]},
    'forest': {'n_estimators': [10, 20, 50, 100]}
}
