import sys

remainArray = [0 for i in range(10)]

for i in range(10):
    N = int(sys.stdin.readline().strip())
    remainArray[i] = N % 42

count = 0

for i in range(10):
    for j in range(i+1, 10):
        if(remainArray[i] == remainArray[j]):
            remainArray[j] = "null"


for i in range(10):
    if(remainArray[i] != "null"):
        count = count + 1

print(count)
