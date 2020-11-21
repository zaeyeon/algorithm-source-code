import sys

N = int(sys.stdin.readline().strip())

numberOfLines = 0
firstNumOfLine = 1
denominator = 0
numerator = 0
i = 0

while firstNumOfLine <= N:
    i = i + 1
    if(firstNumOfLine + i > N):
        if(i % 2 == 0):
            denominator = i - (N - firstNumOfLine)
            numerator = (N - firstNumOfLine) + 1
            break
        if(i % 2 == 1):

            denominator = (N - firstNumOfLine) + 1
            numerator = i - (N - firstNumOfLine)
        
    firstNumOfLine = firstNumOfLine + i

print(f"{numerator}/{denominator}")

    