from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

@ignore_warnings(category=ConvergenceWarning)

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
    'breast-cancer': datasets.load_breast_cancer()
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

std_frame = pd.DataFrame(index=classifiers.keys(), columns=['media', 'dp', 'scores'])

dataset_frames = {
    'iris':             std_frame.copy(),
    'digits':           std_frame.copy(),
    'wine':             std_frame.copy(),
    'breast-cancer':    std_frame.copy()
}

for dataset_name, dataset in datasets.items():
    for classifier_name, classifier in classifiers.items():
        gs = GridSearchCV(estimator=classifier, param_grid=params[classifier_name], scoring='accuracy', n_jobs=-1, cv=4)
        scores = cross_val_score(estimator=gs, X=dataset.data, y=dataset.target, scoring='accuracy', cv=10)
        dataset_frames[dataset_name].loc[classifier_name] = [scores.mean(), scores.std(), scores]

for dataset_name, frame in dataset_frames.items():
    print(dataset_name)
    print(frame, end='\n\n')

    boxplot = pd.DataFrame()

    for classifier_name, classifier in classifiers.items():
        boxplot[classifier_name] = frame.at[classifier_name, 'scores']

    sns.boxplot(data=boxplot, showmeans=True)
    
    plt.title(dataset_name)
    plt.ylabel('scores')
    plt.xlabel('classificadores')

    try:
        os.makedirs('boxplots/part2')
        os.makedirs('csv/part2')
    except FileExistsError:
        pass

    plt.savefig(f"boxplots/part2/{dataset_name}-part2.png")
    
    plt.cla()
    plt.clf()

    csv_table = frame.drop(['scores'], axis=1)
    csv_table.to_csv(f"csv/part2/{dataset_name}-part2.csv")

plt.close()
