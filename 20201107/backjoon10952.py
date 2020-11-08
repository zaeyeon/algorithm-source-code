import sys

try:
    while 1:
        a, b = sys.stdin.readline().split()
        print(int(a) + int(b))
except: exit
26