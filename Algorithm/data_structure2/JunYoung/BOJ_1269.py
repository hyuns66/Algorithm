# 대칭 차집합

import sys

N, M = list(map(int, sys.stdin.readline().split()))

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

var = N + M - 2 * len(A & B)
print(var)

# 교집합: s1 & s2 / s1.intersection(s2)
# 합집합: s1 | s2 / s1.union(s2)
# 차집합: s1 - s2 / s1.difference(s2)
