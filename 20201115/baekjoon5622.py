import sys

inputedStr = sys.stdin.readline().strip()
list1 = list(inputedStr)
count = 0

for i in range(len(list1)):
    if list1[i] == 'A' or list1[i] == 'B' or list1[i] == 'C':
        count = count + 1 + 2
    elif list1[i] == 'D' or list1[i] == 'E' or list1[i] == 'F':
        count = count + 2 + 2
    elif list1[i] == 'G' or list1[i] == 'H' or list1[i] == 'I':
        count = count + 3 + 2
    elif list1[i] == 'J' or list1[i] == 'K' or list1[i] == 'L':
        count = count + 4 + 2
    elif list1[i] == 'M' or list1[i] == 'N' or list1[i] == 'O':
        count = count + 5 + 2
    elif list1[i] == 'P' or list1[i] == 'Q' or list1[i] == 'R' or list1[i] == 'S':
        count = count + 6 + 2
    elif list1[i] == 'T' or list1[i] == 'U' or list1[i] == 'V':
        count = count + 7 + 2
    elif list1[i] == 'W' or list1[i] == 'X' or list1[i] == 'Y' or list1[i] == 'Z':
        count = count + 8 + 2

print(count)        
