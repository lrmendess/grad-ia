def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import math
import pandas as pd

from scipy.spatial import distance
from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels
from sklearn.base import BaseEstimator, ClassifierMixin

class CentroidOneR(BaseEstimator, ClassifierMixin):
    def fit(self, x_train, y_train):
        self.class_  = unique_labels(y_train)
        self.x_train = x_train
        self.y_train = y_train

        self.candidates = list()
        self.predict_table = dict()
        self.predict_table_index = 0

        bins = [len(self.class_)] * len(self.x_train[0])
        bins = preprocessing.KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy='uniform').fit(self.x_train).transform(self.x_train)

        iterations = len(self.x_train[0])

        for i in range(iterations):
            cross = pd.crosstab(bins[:,i], self.y_train)
            rules = self.gen_table_rules(cross)
            self.candidates.append(rules)

        self.predict_table_index = self.best_predict_table_index(bins, self.y_train, self.candidates)
        self.predict_table = self.candidates[self.predict_table_index]

        # Centroide
        selected_column = x_train[:,self.predict_table_index]
        class_lists = dict()
        self.rule_set = dict()

        for k in self.class_:
            class_lists[k] = list()

        for i in range(len(selected_column)):
            class_lists[y_train[i]].append(selected_column[i])

        for key, value in class_lists.items():
            self.rule_set[key] = sum(value) / len(value)

    def predict(self, x_test):
        predict = []

        x_test = x_test[:,self.predict_table_index]

        for i in range (len(x_test)):
            opt_dist = math.inf
            opt_class = 0
            
            for key, value in self.rule_set.items():
                temp_dist = distance.euclidean(x_test[i], value)

                if(opt_dist >= temp_dist):
                    opt_class = key
                    opt_dist = temp_dist

            predict.append(opt_class)

        return predict

    def gen_table_rules(self, df):
        table = dict()
        
        for df_row_index, df_row in df.iterrows():
            df_column_index = self.best_column_index(df_row)
            df_column_name = df.columns[df_column_index]
            table[df_row_index] = df_column_name

        return table

    def best_column_index(self, row):
        best_column_index = 0
        max_value = 0

        for index, element in enumerate(row):
            if element > max_value:
                max_value = element
                best_column_index = index

        return best_column_index

    def best_predict_table_index(self, x_train, y_train, candidates):
        best_candidate_index = 0
        best_accuracy = 0.0

        for candidate_index, candidate in enumerate(candidates):
            predict = list()

            for element in x_train[:,candidate_index]:
                predict.append(candidate[element])
                 
            equals = filter(lambda x: x[0] == x[1], zip(predict, y_train))
            accuracy = len(list(equals)) / len(list(y_train))

            if accuracy >= best_accuracy:
                best_accuracy = accuracy
                best_candidate_index = candidate_index

        return best_candidate_index

if __name__ == '__main__':
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

    centroid_oner = CentroidOneR()
    centroid_oner.fit(x_train, y_train)

    predict = centroid_oner.predict(x_test)
    accuracy = centroid_oner.score(x_test, y_test)

    print(f"Predict: {predict}")
    print(f"Accuracy: {accuracy}")