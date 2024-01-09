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

# 리스트에서 in 연산은 O(n)으로 매우 느리다.
