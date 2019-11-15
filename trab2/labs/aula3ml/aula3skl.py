def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import numpy as np

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

iris = datasets.load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

knn = KNeighborsClassifier()

scores = cross_val_score(knn, iris.data, iris.target, cv=5)

grade = {'n_neighbors': [1, 3, 5]}

gs = GridSearchCV(estimator=knn, param_grid=grade, scoring='accuracy', cv=10)
gs = gs.fit(x_train, y_train)

print(gs.best_score_)
print(gs.best_params_)
print(gs.cv_results_.keys())
print(gs.cv_results_['split8_test_score'][0])
print(gs.cv_results_['split9_test_score'])

parciais1 = np.array([  
    gs.cv_results_['split0_test_score'][0],
    gs.cv_results_['split1_test_score'][0],
    gs.cv_results_['split2_test_score'][0],
    gs.cv_results_['split3_test_score'][0],
    gs.cv_results_['split4_test_score'][0],
    gs.cv_results_['split5_test_score'][0],
    gs.cv_results_['split6_test_score'][0],
    gs.cv_results_['split7_test_score'][0],
    gs.cv_results_['split8_test_score'][0],
    gs.cv_results_['split9_test_score'][0]
])

parciais2 = np.array([
    gs.cv_results_['split0_test_score'][1],
    gs.cv_results_['split1_test_score'][1],
    gs.cv_results_['split2_test_score'][1],
    gs.cv_results_['split3_test_score'][1],
    gs.cv_results_['split4_test_score'][1],
    gs.cv_results_['split5_test_score'][1],
    gs.cv_results_['split6_test_score'][1],
    gs.cv_results_['split7_test_score'][1],
    gs.cv_results_['split8_test_score'][1],
    gs.cv_results_['split9_test_score'][1]
])

print(parciais1)
print(parciais2)

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=[parciais1, parciais2], showmeans=True)
plt.show()

gs = GridSearchCV(estimator = knn, param_grid = grade, scoring = 'accuracy', n_jobs = -1)
scores = cross_val_score(gs, x_train, y_train, scoring = 'accuracy', cv = 5)
print('CV Accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))
print(scores)