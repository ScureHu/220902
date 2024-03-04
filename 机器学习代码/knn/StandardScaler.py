import numpy as np


class StandardScaler:
    def __init__(self):
        self.mean_ = None
        self.scal_ = None

    def fit(self, x_train):
        self.mean_ = np.array([np.mean(x_train[:, lie]) for lie in range(x_train.shape[1])])
        self.scal_ = np.array([np.std(x_train[:, lie]) for lie in range(x_train.shape[1])])
        return self

    def tranform(self, x):
        return np.array([(x[:, lie] - self.mean_[lie]) / self.scal_[lie] for lie in range(x.shape[1])])
