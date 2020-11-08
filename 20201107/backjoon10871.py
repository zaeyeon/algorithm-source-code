import sys

N, X = sys.stdin.readline().split()
A = [0 for i in range(int(N))]

A = sys.stdin.readline().split()

for i in range(int(N)):
    if(int(A[i]) < int(X)):
        print(A[i], end=" ")
