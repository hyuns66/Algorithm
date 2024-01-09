"""
2, 3, 6
0 0 1 0 1 0 1 0 1 0 1 0 1 0 1
0 0 1 1 1 1 2 0 1 1 1 0 2 0 1
0 0 1 1 1 0 2 0 1 1 1 0 2 0 1
"""

import sys

T = int(sys.stdin.readline())
answer = list()
for _ in range(T):
    N = int(sys.stdin.readline())
    collection = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M+1)
    dp[0] = 1
    for idx, coin in enumerate(collection):
        for i in range(M+1):
            if i - coin < 0:
                continue
            dp[i] += dp[i-coin]
    answer.append(dp[-1])
for a in answer:
    print(a)