# 2+1 세일

import sys

N = int(sys.stdin.readline())
priceList = []
for i in range(N):
    c = int(sys.stdin.readline())
    priceList.append(c)

priceList.sort(reverse=True)

sum = 0
for i in range(N):
    if ((i + 1) % 3) != 0:
        sum = sum + priceList[i]

print(sum)
