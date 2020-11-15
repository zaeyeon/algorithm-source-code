import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    strList = list(S)
    resultList = []
    for j in range(len(strList)):
        for w in range(R):
            resultList.append(strList[j])

    print(''.join(resultList))    
    


