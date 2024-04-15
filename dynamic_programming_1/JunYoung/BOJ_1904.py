# 01타일

import sys

n = int(sys.stdin.readline())
memo = [0 for _ in range(n+2)]

memo[1] = 1 # 1
memo[2] = 2 # 11, 00


for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746

print(memo[n])