A = [
    [0.405, 0.05, 0.04, 0.0, 0.09],
    [-0.061, 0.53, 0.073, 0.11, -0.06],
    [0.07, -0.036, 0.38, 0.03, 0.02],
    [-0.05, 0.0, 0.066, 0.58, 0.23],
    [0.0, 0.081, -0.05, -0.0, 0.41]
]
B = [-1.475, -2.281, -0.296, 0.492, 1.454]


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

    def _check_first_condition(self):
        result = []
        for row in self.A:
            if abs(row[0]) > abs(sum(map(abs, row[1:]))):
                result.append(True)
            else:
                result.append(False)
        return result

    def _check(self):
        for i in range(len(self.x_old)):
            if abs(self.x_old[i] - self.x_new[i]) >= self.epsilon:
                return False
        return True

    def iterate(self):
        self.x_new = self.B[:]
        self.iterations += 1
        for index, row in enumerate(self.A):
            denominator_sum = 0
            for idx, item in enumerate(row):
                if not idx == index:
                    denominator_sum += row[idx] * self.x_old[idx]
            self.x_new[index] = (self.x_new[index] - denominator_sum) / row[index]

    def solve(self):
        if self._check_first_condition():
            while True:
                self.iterate()  # iterate function
                print(f"iteration {self.iterations}", self.x_new)
                if self._check():
                    break
                else:
                    self.x_old = self.x_new
        else:
            print("Умова не виконана")


x = LinAlgSimpleIteration(A, B, epsilon= 0.0000001)
x.solve()
