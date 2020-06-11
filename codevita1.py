# matrix = [[0, 3, 9, 6],
#           [1, 4, 4, 5],
#           [8, 2, 5, 4],
#           [1, 8, 5, 9]]

#with python list


matrix = []
n = int(input())

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
    temp = []

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
            matrix.pop(0) # removing Row
        else:
            k = matrix[0][1]
            score = (score//2) + k
            
            for i in matrix: # removing column
                del i[0]

    except:
        try:
            k = matrix[0][1]
            score = (score//2) + k
            for i in matrix: # removing column
                del i[0]
        except:
            k = matrix[1][0]
            score = (score//2) + k
            matrix.pop(0) # removing Row

print(score)
