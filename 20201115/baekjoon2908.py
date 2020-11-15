import sys

num1, num2 = sys.stdin.readline().split()
num1List = list(num1)
num2List = list(num2)

num1List.reverse()
num2List.reverse()

revNum1 = int(''.join(num1List))
revNum2 = int(''.join(num2List))

if revNum1 > revNum2:
    print(revNum1)
else:
    print(revNum2)