import sys
A = [0 for i in range(9)]

for i in range(9):
    A[i] = int(sys.stdin.readline().strip())

max = A[0]
maxIndex = 0

for i in range(9):
    if(max < A[i]):
        max = A[i]
        maxIndex = i

print(max)
print(maxIndex+1)