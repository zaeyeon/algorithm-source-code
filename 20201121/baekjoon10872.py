import sys

N = int(sys.stdin.readline().strip())

def getFactorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    elif (n > 1):
        return n*getFactorial(n-1)
    else:
        return

print(getFactorial(N))
