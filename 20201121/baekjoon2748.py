import sys

N = int(sys.stdin.readline().strip())
numArray = [0 for j in range(N+1)]

for i in range(N+1):
    if(i == 0):
        numArray[i] = 0
    elif(i == 1):
        numArray[i] = 1
    else:
        numArray[i] = numArray[i-2] + numArray[i-1]


print(numArray[N])
    
