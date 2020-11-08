inputYear = int(input())
if(inputYear % 4 == 0 and inputYear % 100 != 0):
    print(1)
elif(inputYear % 100 == 0 and inputYear % 400 != 0):
    print(0)
elif(inputYear % 400 == 0):
    print(1)
else:
    print(0)
