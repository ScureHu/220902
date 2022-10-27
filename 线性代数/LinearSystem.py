from Vector import Vector
from Matrix import Matrix


class LinearSystem:
    def __init__(self, A, b):
        assert A.row_num() == len(b), "xxxx"
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                       for i in range(self._m)]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list())
                       for i in range(self._m)]

    def _max_row(self, index, n):
        ret, index = self.Ab[index][index], index
        for i in range(index + 1, n):
            if self.Ab[i][index] > ret:
                ret, index = self.Ab[i][index], i
        return index

    def _forward(self):
        n = self._m
        for i in range(n):
            max_row = self._max_row(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def _backward(self):
        n = self._m
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])


def inv(A):
    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    ls.gauss_jordan_elimination()
    invA = [[row[i] for i in range(n, 2 * n)] for row in ls.Ab]
    return Matrix(invA)


if __name__ == "__main__":
    # A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    # b = Vector([7, -11, 1])
    # ls = LinearSystem(A, b)
    # ls.gauss_jordan_elimination()
    # ls.fancy_print()
    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
