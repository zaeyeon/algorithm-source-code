import sys

caseCount = int(sys.stdin.readline().strip())
caseArray = [0 for i in range(caseCount)]
scoreArray = [0 for i in range(caseCount)]

for i in range(caseCount):
    tmpCase = sys.stdin.readline().strip()
    tmpCaseArray = list(tmpCase)

    answerCount = 0
    tmpScore = 0
    scoreArray[i] = tmpScore

    for j in range(len(tmpCaseArray)):
        if(tmpCaseArray[j] == "O"):
            answerCount = answerCount + 1
            tmpScore = tmpScore + answerCount
            scoreArray[i] = tmpScore

        elif(tmpCaseArray[j] == "X"):
            answerCount = 0

for i in range(caseCount):
    print(scoreArray[i])

    