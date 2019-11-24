def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import math
import numpy as np
import pandas as pd

from collections import Counter
from scipy.spatial import distance
from sklearn import datasets, preprocessing
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin

class Centroid(BaseEstimator, ClassifierMixin):
	def fit(self, x_train, y_train):
		self.centroids = dict()

		group_by = Counter(y_train)

		for key, value in group_by.items():
			self.centroids[key] = [0] * len(x_train[0])

		for index, element in enumerate(x_train):
			self.centroids[y_train[index]] += element

		for key, value in self.centroids.items():
			self.centroids[key] = value / group_by[key]

	def predict(self, x_train):
		predict = []

		for element in x_train:
			best_class = 0
			best_distance = math.inf
			
			for key, value in self.centroids.items():
				d = distance.euclidean(element, value)

				if(best_distance >= d):
					best_class = key
					best_distance = d

			predict.append(best_class)

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