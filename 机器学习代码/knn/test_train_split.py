import numpy as np


def test_train_split(x, y, test_ratio=0.2, seed=None):
    if (seed != None):
        np.random.seed(seed)
    shuffed_indexes = np.random.permutation(len(x))
    test_size = int(len(x) * test_ratio)
    x_train = x[shuffed_indexes[test_size:]]
    y_train = y[shuffed_indexes[test_size:]]
    x_test = x[shuffed_indexes[:test_size]]
    y_test = y[shuffed_indexes[:test_size]]
    return x_train, y_train, x_test, y_test
