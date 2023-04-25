#ATM

import sys
from collections import deque

N = int(sys.stdin.readline())
timeCost = list(map(int, sys.stdin.readline().split()))

timeCost.sort()
#print(timeCost)

sum = 0
for length in range(1,len(timeCost)+1):
    for i in range(0,length):
        sum += timeCost[i]
        #print(str(timeCost[i])+"더해짐")

print(sum)
