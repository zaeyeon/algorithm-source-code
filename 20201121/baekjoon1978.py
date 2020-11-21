import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(1, numbers[i]):
        if j != 1:
            if(numbers[i] % j == 0):
                numbers[i] = True
        
for j in numbers:
    if j != 1 or j != True:
        count = count + 1

print(count)
