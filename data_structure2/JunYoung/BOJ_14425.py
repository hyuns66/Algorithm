# 문자열 집합

import sys

N, M = map(int, sys.stdin.readline().split())

S = set()
for _ in range(N):
    S.add(sys.stdin.readline().strip())

count = 0
for _ in range(M):
    userInput = sys.stdin.readline().strip()
    if userInput in S:
        count += 1

print(count)


