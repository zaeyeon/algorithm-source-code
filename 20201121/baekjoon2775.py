import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    k = int(sys.stdin.readline().strip()) + 1
    n = int(sys.stdin.readline().strip())
    array = [[0 for col in range(n)] for row in range(k)]

    for j in range(k):
        for w in range(n):
            if j == 0:
                array[j][w] = w+1
            else:
                array[j][w] = array[j-1][w] + array[j][w - 1]
    
    print(array[k-1][n-1])


