import math
import sys

T = int(sys.stdin.readline().strip())
result = [0 for j in range(T)]



for i in range(T):
    H, W, N = sys.stdin.readline().split()
    H = int(H)
    W = int(W)
    N = int(N)

    hosu = math.ceil(N/H)
    floors = (H - (H*hosu - N))
    if hosu < 10:
        result[i] = (str(floors) + "0" + str(hosu))
    else:
        result[i] = (str(floors) + str(hosu))


for j in result:
    print(j)

    