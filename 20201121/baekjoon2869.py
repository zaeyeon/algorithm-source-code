import sys
import math

A, B, V = sys.stdin.readline().split()

A = int(A)
B = int(B)
V = int(V)

day = math.ceil((V-B)/(A-B))
    
    
print(day)
    