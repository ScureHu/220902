import numpy as np
from math import sqrt
from collections import Counter

def KNN_calssify(k, X_train, Y_train, x):
    assert 1 <= k <= X_train.shape[0], "k must be vaild"
    assert X_train.shape[0] == Y_train.shape[0],\
        "the size of X_train must equal to the size of y_train"
    assert X_train.shape[1] == x.shape[0]
    distance = [sqrt(np.sum((x_train - x) ** 2)) for x_train in X_train]
    nearrest = np.argsort(distance)
    topk_y = [Y_train[i] for i in nearrest[:k]]
    votes = Counter(topk_y)
    return votes.most_common(1)[0][0]