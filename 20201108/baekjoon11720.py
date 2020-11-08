import sys

N = int(sys.stdin.readline().strip())
numberArr = [0 for i in range(N)]
numberStr = sys.stdin.readline().strip()
numberArr = list(numberStr)
numberArr = list(map(int, numberArr))

print(sum(numberArr))