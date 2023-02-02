import numpy as np
from math import sqrt
from collections import Counter


class KNNClassifier:
    def __init__(self, k):
        """初始化"""
        self._x_train = None
        self._y_train = None
        self.k = k

    def fit(self, x_train, y_train):
        self._y_train = y_train
        self._x_train = x_train
        return self

    def predict(self, x_predict):
        assert self._x_train is not None and self._y_train is not None, "must fit before predict"
        assert self._x_train.shape[1] == x_predict.shape[1], "x_predict must equal x_train"
        y_predict = [self._predict(x) for x in x_predict]
        return np.array(y_predict)

    def _predict(self, x_train):
        distance = [sqrt(np.sum((x - x_train) ** 2)) for x in self._x_train]
        nearMax = np.argsort(distance)
        y_votes = [self._y_train[i] for i in nearMax[:self.k]]
        vores = Counter(y_votes)
        return vores.most_common(1)[0][0]
