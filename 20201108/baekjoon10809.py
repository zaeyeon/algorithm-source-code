import sys

S = sys.stdin.readline().strip()
strArray = list(S)
tmpArray = []
alphaStr = "abcdefghijklmnopqrstuvwxyz"
alphaArr = list(alphaStr)
result = [-1 for i in range(26)]

for i in range(len(strArray)):
    for j in range(i+1, len(strArray)):
        if strArray[i] == strArray[j]:
            strArray[j] = 0
             


for i in range(len(strArray)):
    for j in range(len(alphaArr)):
        if strArray[i] == alphaArr[j]:
            result[j] = i
            break

for i in range(len(result)):
    print(result[i], end=" ")
    