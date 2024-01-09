# 원상 복구 (small)

import sys

N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

rollBack = [0 for i in range(N)]
for _ in range(K):
    # print("---------------------")
    # rollBack = [0 for i in range(N)]
    for i in range(N):
        rollBack[D[i] - 1] = S[i]
        # print(f"i번째: {i}, S[i]: {S[i]}, S= {S}")
        # print(f"rollBack: {rollBack}")

    S = rollBack[:]
    # print(f"S:{S}")

for i in S:
    print(i, end=" ")

# ★ 얕은 복사, 깊은 복사
# listA = listB 이렇게 냅다 넣으면 둘이 같은 포인터를 가르키게 된다.
# [:]를 쓰면 복사하 수 있으나, 안에 객체까지 깊은 복사를 시키진 못한다.
# 이럴 때는 import copy, listA = copy.deepcopy(listB)를 써주면 된다.
# https://wikidocs.net/16038
