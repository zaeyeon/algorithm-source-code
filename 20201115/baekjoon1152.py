import sys

inputStr = sys.stdin.readline().strip()

wordList = inputStr.split(" ")
count = 0

for i in range(len(wordList)):
    if(wordList[i].strip() != ""):
        count = count+1

print(count)