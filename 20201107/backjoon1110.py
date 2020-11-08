import sys

N = int(sys.stdin.readline().strip())

if N < 10:
    N = "0" + str(N)

result = int(N)
count = 0

while True:
    units = result % 10
    tens = int(result / 10)
    sumUnits = (units + tens) % 10
    result = int(str(units) + str(sumUnits))
    count = count+1
    if(int(result) == int(N)):
        break

print(count)


