import sys

subCount = int(sys.stdin.readline().strip())
scoArray = [0 for i in range(subCount)]

scoArray = sys.stdin.readline().split()
scoArray = list(map(int, scoArray))
max = scoArray[0]
sum = 0

for i in range(len(scoArray)):
    if(max < scoArray[i]):
        max = scoArray[i]

for i in range(len(scoArray)):
    scoArray[i] = scoArray[i]/max*100
    sum = sum + scoArray[i]
    
print(sum/subCount)

