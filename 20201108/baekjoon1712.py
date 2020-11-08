import sys

A, B, C = sys.stdin.readline().split()
A = int(A)
B = int(B)
C = int(C)
N = 1

if(B >= C):
    N = -1
else:
    N = int(A/(C-B))+1
    
print(N)
