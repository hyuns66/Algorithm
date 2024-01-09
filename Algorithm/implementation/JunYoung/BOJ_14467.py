# 소가 길을 건너간 이유1

import sys
N = int(sys.stdin.readline())

whereCow = {}
minCross = 0
for _ in range(N):
    cow, road = map(int, sys.stdin.readline().split())
    if cow in whereCow:
        if whereCow[cow] != road:
            minCross += 1
    whereCow[cow] = road

print(minCross)
