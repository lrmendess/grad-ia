def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels
from sklearn.base import BaseEstimator, ClassifierMixin
import pandas as pd
import numpy as np
from collections import Counter
from scipy.spatial import distance
import math

class Centroid(BaseEstimator, ClassifierMixin):
	
	def __init__(self):
		pass

	def fit(self, x_train, y_train):
		self.centroids = dict()
		group_by = Counter(y_train)
		
		# Construindo dict
		for key, _ in group_by.items():
			self.centroids[key] = np.zeros(len(x_train[0]))

		# Somando todas as distancias
		for i in range (0, len(x_train)):
			self.centroids[y_train[i]] += x_train[i]

		# Dividindo pelo numero de items
		for key, value in self.centroids.items():
			self.centroids[key] = value / group_by[key]

	def predict(self, x_train):
		predict = []

		for i in range (len(x_train)):
			opt_dist = math.inf
			opt_class = 0
			
			for key, value in self.centroids.items():
				temp_dist = distance.euclidean(x_train[i], value)
				if(opt_dist >= temp_dist):
					opt_class = key
					opt_dist = temp_dist

			predict.append(opt_class)

		return predict


if __name__ == '__main__':
	iris = datasets.load_iris()
	x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

	centroid = Centroid()
	centroid.fit(x_train, y_train)

	predict = centroid.predict(x_test)
	accuracy = centroid.score(x_test, y_test)

	print(f"Predict: {predict}")
	print(f"Accuracy: {accuracy}")