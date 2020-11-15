import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"

N = int(sys.stdin.readline().strip())
wordList = [0 for i in range(N)]
resultList = [True for i in range(N)]

for i in range(N):
    wordList[i] = sys.stdin.readline().strip()

    for alp in alphabet:
        if(wordList[i].count(alp) > 1):
            tmpWordList = list(wordList[i])
            indexList = list(filter(lambda e:tmpWordList[e] == alp, range(len(tmpWordList))))
            
            for j in range(len(indexList)):
                if j != len(indexList) - 1:
                    if(indexList[j+1] - indexList[j] > 1):
                        resultList[i] = False
                        break

print(resultList.count(True))