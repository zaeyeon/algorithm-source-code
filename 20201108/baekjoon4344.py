import sys

caseCount = int(sys.stdin.readline().strip())
ratioArray = [0 for i in range(caseCount)]

for i in range(caseCount):
    tmpArray = sys.stdin.readline().split()
    tmpStuCount = int(tmpArray[0])
    del tmpArray[0]
    tmpArray = list(map(int, tmpArray))
    tmpSum = 0
    tmpAvg = 0
    tmpRatio = 0
    overCount = 0

    for j in range(tmpStuCount):
        tmpSum = tmpSum + tmpArray[j]

    tmpAvg = tmpSum / tmpStuCount

    for w in range(tmpStuCount):
        if(tmpAvg < tmpArray[w]):
            overCount = overCount + 1
    
    tmpRatio = overCount / tmpStuCount * 100

    ratioArray[i] = tmpRatio

for i in range(caseCount):
    print(f"{'%.3f' % ratioArray[i]}%")


