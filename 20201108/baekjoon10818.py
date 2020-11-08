import sys

N = int(sys.stdin.readline().strip())

A = [0 for i in range(N)]

A = sys.stdin.readline().split()

A = list(map(int, A))

max = A[0]
min = A[0]

for i in range(N):
    if(max < A[i]):
        max = A[i]
    
    if(min > A[i]):
        min = A[i]

print(min, max)

    