import sys

n = int(sys.stdin.readline().strip())

for (i) in range(n):
    staNum = i+1
    spaNum = n - (i+1)

    for spa in range(spaNum):
        print(" ", end="")
    
    for sta in range(staNum):
        print("*", end="")

    print()
