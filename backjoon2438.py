import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
