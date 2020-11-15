import sys

word = sys.stdin.readline().strip()
upperWord = word.upper()

wordList = list(upperWord)
tmpList = list(set(wordList))

countList = []
result = ""
maxCount = 0

for i in range(len(tmpList)):
    tmpCount = wordList.count(tmpList[i])
    
    if(tmpCount >= maxCount):
        if(tmpCount == maxCount):
            maxCount = tmpCount
            result = "?"
        elif(tmpCount > maxCount):
            maxCount = tmpCount
            result = tmpList[i]

print(result)

