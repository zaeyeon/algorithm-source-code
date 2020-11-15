import sys

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

inputStr = sys.stdin.readline().strip()

while True:
    tmp = inputStr
    for char in croatia:
        if char in tmp:
            ind = tmp.index(char)
            c = len(char)
            tmp = tmp[:ind] + "/" + tmp[ind+c:]
            break
    if tmp != inputStr:
        inputStr = tmp
    else:
        break

print(len(inputStr))
