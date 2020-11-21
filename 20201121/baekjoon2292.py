import sys

N = int(sys.stdin.readline().strip())
unit = 1
count = 1

while unit < N:
    unit = unit + (count * 6)
    count = count + 1

print(count)