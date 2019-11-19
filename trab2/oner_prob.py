def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

import pandas as pd

from random import uniform, choice

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels
from sklearn.base import BaseEstimator, ClassifierMixin

class OneRProb(BaseEstimator, ClassifierMixin):
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

    def predict(self, x_test):
        predict = list()

        bins = [len(self.class_)] * len(x_test[0])
        bins = preprocessing.KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy='uniform').fit(x_test).transform(x_test)

        for element in bins[:,self.predict_table_index]:
            if element in self.predict_table:
                predict.append(self.predict_table[element])
            else:
                predict.append(choice(list(self.predict_table.items()))[1])

        return predict

    def gen_table_rules(self, df):
        table = dict()
        
        for df_row_index, df_row in df.iterrows():
            df_column_index = self.best_column_index(df_row)
            df_column_name = df.columns[df_column_index]
            table[df_row_index] = df_column_name

        return table

    def best_column_index(self, row):
        sum_ = sum([r for r in row])
        reasons = [(i, r / sum_) for i, r in enumerate(row)]
        reasons.sort(key=lambda e: e[1], reverse=True)

        roulette, sum_ = list(), 0

        for r in reasons:
            sum_ += r[1]
            roulette.append((r[0], sum_))

        prob = uniform(0, 1)

        for r in roulette:
            if prob <= r[1]:
                return r[0]

        return choice([x for x in range(len(row))])

    def best_predict_table_index(self, x_train, y_train, candidates):
        best_candidate_index = 0
        best_accuracy = 0.0

        for cadidate_index, candidate in enumerate(candidates):
            predict = list()

            for element in x_train[:,cadidate_index]:
                predict.append(candidate[element])
                
            equals = filter(lambda x: x[0] == x[1], zip(predict, y_train))
            accuracy = len(list(equals)) / len(list(y_train))

            if accuracy >= best_accuracy:
                best_accuracy = accuracy
                best_candidate_index = cadidate_index

        return best_candidate_index

if __name__ == '__main__':
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

    oner = OneRProb()
    oner.fit(x_train, y_train)

    predict = oner.predict(x_test)
    accuracy = oner.score(x_test, y_test)

    print(f"Predict: {predict}")
    print(f"Accuracy: {accuracy}")
