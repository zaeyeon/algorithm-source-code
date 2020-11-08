import sys

def getHansu(n):
    a1 = list(str(n))
    a1 = list(map(int, a1))

    if len(a1) == 1:
        return True
    elif len(a1) > 1:
        dif = a1[1] - a1[0]
        for i in range(len(a1)-1):
            if a1[i+1] - a1[i] != dif:
                return False
    
    return True
        
    
N = int(sys.stdin.readline().strip())
hansuCount = 0

for i in range(1, N+1):
    if getHansu(i) == True:
        hansuCount = hansuCount + 1

print(hansuCount)

        
        