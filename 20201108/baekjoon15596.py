
def solve(a: list):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]

    print("sum", sum)
    return sum

'''
numberArray = input().split()
numberArray = list(map(int, numberArray))

print(numberArray)
sum(numberArray)
'''