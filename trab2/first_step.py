def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

from oner_prob import OneRProb
from centroid import Centroid
from zeror import ZeroR
from oner import OneR

from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets

datasets = {
    'iris': datasets.load_iris(),
    'digits': datasets.load_digits(),
    'wine': datasets.load_wine(),
    'breast_cancer': datasets.load_breast_cancer()
}

classifiers = {
    'zeror': ZeroR(),
    'oner': OneR(),
    'oner_prob': OneRProb(),
    'gaussian': GaussianNB(),
    'centroid': Centroid()
}

std_frame = pd.DataFrame(index=classifiers.keys(), columns=['media', 'dp', 'scores'])

dataset_frames = {
    'iris':             std_frame.copy(),
    'digits':           std_frame.copy(),
    'wine':             std_frame.copy(),
    'breast_cancer':    std_frame.copy()
}

for dataset_name, dataset in datasets.items():
    for classifier_name, classifier in classifiers.items():
        scores = cross_val_score(estimator=classifier, X=dataset.data, y=dataset.target, cv=10)
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
        os.makedirs('boxplots/part1')
        os.makedirs('csv/part1')
    except FileExistsError:
        pass

    plt.savefig(f"boxplots/part1/{dataset_name}_part1.png")
    
    plt.cla()
    plt.clf()
    
    csv_table = frame.drop(['scores'], axis=1)
    csv_table.to_csv(f"csv/part1/{dataset_name}_part1.csv")

plt.close()
