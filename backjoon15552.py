import sys

amount = int(sys.stdin.readline().rstrip())

for i in range(amount):
    a, b = sys.stdin.readline().split()
    print(int(a) + int(b))

    