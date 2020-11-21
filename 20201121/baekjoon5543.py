import sys

minHam = 0
minBev = 0

for i in range(3):
    price = int(input())
    if(i == 0): minHam = price
    if minHam > price:
        minHam = price

for i in range(2):
    price2 = int(input())
    if(i == 0): minBev = price2
    if minBev > price2:
        minBev = price2


print(minHam+minBev-50)
    