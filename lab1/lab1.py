EPSILON = 0.000000001
from numpy import linalg
from time import sleep
A = [
    [0.405, 0.05, 0.04, 0.0, 0.09],
    [-0.061, 0.53, 0.073, 0.11, -0.06],
    [0.07, -0.036, 0.38, 0.03, 0.02],
    [-0.05, 0.0, 0.066, 0.58, 0.23],
    [0.0, 0.081, -0.05, -0.0, 0.41]
]

B = [-1.475, -2.281, -0.296, 0.492, 1.454]
X = [0,0,0,0,0]

COUNTER = 0
print(linalg.solve(A, B))


def check_first_condition(A):
    result = []
    for row in A:
        if abs(row[0]) > abs(sum(map(abs, row[1:]))):
            result.append(True)
        else:
            result.append(False)
    print(result)
    return result

def check(old_x, new_x, e):
    for i in range(len(old_x)):
        if abs(old_x[i] - new_x[i]) >= e:
            return False
    return True

def iteration_function(X,A, B):
    x_old = X[:]
    x_new = B[:]
    for index, row in enumerate(A):
        x_new[index] = x_new[index]/row[index]
        for idx, item in enumerate(row):
            if not idx == index:
                x_new[index] -= row[idx]*x_old[idx]/row[index]
    return x_new


if __name__ == '__main__':
    if check_first_condition(A):
        counter = 0
        while True:
            counter += 1
            x_new = iteration_function(X, A, B)
            print(f"iteration {counter}",x_new)
            if check(X, x_new, EPSILON):
                print(x_new, counter)
                break
            else:
                X = x_new
    else:
        print("LOL")