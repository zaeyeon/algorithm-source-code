import sys

amount = int(sys.stdin.readline().strip())

for i in range(amount):
    a, b = sys.stdin.readline().split()
    print(f"Case #{i+1}: {a} + {b} = {int(a) + int(b)}")
