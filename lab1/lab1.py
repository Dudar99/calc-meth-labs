A = [
    [0.38, -0.05, 0.01, 0.02, 0.07],
    [0.052, 0.595, 0.0, -0.04, 0.04],
    [0.03, 0.0, 0.478, -0.14, 0.08],
    [-0.06, 0.126, 0.0, 0.47, -0.02],
    [0.25, 0.0, 0.09, 0.01, 0.56]
]
B = [-2.32, -2.544, 3.238, -1.534, -0.12]


class LinAlgSimpleIteration:
    def __init__(self, a, b, epsilon=0.00001):
        """
        :param A: koef of linear equations
        :param B: koef of free members
        """
        self.iterations = 0
        self.A = a
        self.B = b
        self.X = [0] * len(A)
        self.epsilon = epsilon
        self.x_old = self.X[:]
        self.x_new = self.B[:]

    def __str__(self):
        for idx, item in enumerate(self.x_new):
            print(idx, -self.x_new[idx])
        return ""

    def _check_first_condition(self):
        result = []
        for row in self.A:
            if abs(row[0]) > abs(sum(map(abs, row[1:]))):
                result.append(True)
            else:
                result.append(False)
        return result

    def _iterate(self):
        self.x_new = self.B[:]
        self.iterations += 1
        for index, row in enumerate(self.A):
            denominator_sum = self.x_old[index] + self.B[index]
            for idx, item in enumerate(row):
                denominator_sum -= row[idx] * self.x_old[idx]
            self.x_new[index] = denominator_sum

    def solve(self):
        if self._check_first_condition():
            while True:
                self._iterate()  # iterate function
                print(f"iteration {self.iterations}", self.x_new)
                if all([abs(a - b) < self.epsilon for a, b in zip(self.x_new, self.x_old)]):
                    break
                else:
                    self.x_old = self.x_new
        else:
            print("Умова не виконана")

    def resignation(self):
        print("Нев'язка:")
        for i in range(len(self.x_new)):
            _sum = 0
            for j in range(len(self.A[i])):
                _sum += self.A[i][j] * self.x_new[j]
            print(f"(f - Ax){i} = {self.B[i] - _sum}")


class LinalgZeidel(LinAlgSimpleIteration):

    def _iterate(self):
        self.x_new = self.B[:]
        self.iterations += 1
        for index, row in enumerate(self.A):
            denominator_sum = 0
            for idx, item in enumerate(row):
                if not idx == index:
                    if idx < index:
                        denominator_sum += row[idx] * self.x_new[idx]
                    else:
                        denominator_sum += row[idx] * self.x_old[idx]
            self.x_new[index] = (self.x_new[index] - denominator_sum) / row[index]


if __name__ == '__main__':
    # x = input("Enter precision:")
    x = LinalgZeidel(A, B, epsilon=0.001)
    x.solve()
    print(x)
    x.resignation()

