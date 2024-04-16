# 동전

import sys

n, k = map(int, sys.stdin.readline().split())

coins = set()
for i in range(n):
    coins.add(int(sys.stdin.readline()))

dp = [sys.maxsize for _ in range(k + 1)]  # i가치의 동전을 만들기 위한 최소 개수

for coin in coins:
    if coin > k:  # 동전금액이 k보다 넘으면 의미 x
        continue
    else:
        dp[coin] = 1

for val in range(1, k + 1):
    for coin in coins:
        if coin > k or val - coin < 1:  # 동전금액이 k보다 넘으면 의미 x
            continue
        else:
            dp[val] = min(dp[val], dp[val - coin] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])

#top-down으로 했는데, 안되고 bottom-up으로 했는데 되네..?!