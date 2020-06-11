import numpy as np

n = int(input())

matrix = []

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
    temp = []

matrix = np.array(matrix)

score = 0
k = 0
for i in range(2*n):

    try:
        if matrix[0][1]:
            pass
    except:
        try:
            if matrix[1][0]:
                pass
        except:
            break

    try:
        if matrix[0][1] > matrix[1][0]:
            k = matrix[1][0]
            score = (score//2) + k
            matrix = np.delete(matrix, 0, 0)
        else:
            k = matrix[0][1]
            score = (score//2) + k
            matrix = np.delete(matrix, 0, 1)

    except:
        try:
            k = matrix[0][1]
            score = (score//2) + k
            matrix = np.delete(matrix, 0, 1)
        except:
            k = matrix[1][0]
            score = (score//2) + k
            matrix = np.delete(matrix, 0, 0)

print(score)
