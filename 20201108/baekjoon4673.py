def d(n):
    sum = n
    tmpArray = list(str(n))
    tmpArray = list(map(int, tmpArray))
    for i in range(len(tmpArray)):
        sum = sum + tmpArray[i]

    return sum

resultArr = []
s1 = set([])

for i in range(1, 10001):
    s1.add(d(i))

s2 = set(range(1, 10001))
s3 = sorted(list(s2-s1))

for i in range(len(s3)):
    print(s3[i])