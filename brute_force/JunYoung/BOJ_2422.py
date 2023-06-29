# 한윤정이 이탈리아 가서 아이스크림을 사먹는데

import sys
import math

N, M = map(int, sys.stdin.readline().split())
dontMix = []

for i in range(M):
    dontMix.append(tuple(map(int, sys.stdin.readline().split())))

dM = {}
for i in range(M):
    num = []
    for n in range(N):
        num.append(n + 1)

    for j in dontMix[i]:
        num.remove(j)
    for j in num:
        dM[(tuple(sorted(tuple(dontMix[i]) + (j,))))] = 1

# print(len(dM))
c3 = math.factorial(N) // (math.factorial(3) * math.factorial(N - 3))
# print(c3)

print(c3 - len(dM))

# math.factorial 사용해 combination 구할 수 있다. => comb함수는 파이썬 3.8부터 지원됨
# dictionary의 키 값 또는 set안에 들어갈 수 있는 애들은 hashable한 녀석들이다.
