import sys

sum = 0

for i in range(5):
    score = int(sys.stdin.readline().strip())
    if(score < 40):
        score = 40
    
    sum = sum + score

print(int(sum/5))