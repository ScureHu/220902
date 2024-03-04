import numpy as np


class SimpleLinearRegression:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        num = 0.0
        d = 0.0
        hs_train = np.hstack([np.ones(x_train.shape(0), 1), x_train])
        np.linalg.inv(hs_train.T.dot(hs_train)).dot(hs_train.T).dot(y_train)
        self.a_ = hs_train.T.dot(y_train) / (hs_train.T.dot(hs_train))
        num = np.dot(x_train - x_mean, y_train - y_mean)
        d = np.dot(x_train - x_mean, x_train - x_mean)
        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

    def predict(self, x_test):
        y_pridict = np.array([self._predict(x) for x in x_test])
        return y_pridict

    def _predict(self, x):
        return x * self.a_ + self.b_
