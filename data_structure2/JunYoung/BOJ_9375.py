# 패션왕 신해빈

import sys
T = int(sys.stdin.readline())

answer = []
for _ in range(T):
    N = int(sys.stdin.readline())
    closet = {}
    for _ in range(N):
        cloth, category = map(str, sys.stdin.readline().split())
        if category in closet:
            closet[category] = closet[category] + [cloth]
        else:
            closet[category] = [cloth]

    categoryNum = len(closet.keys())


