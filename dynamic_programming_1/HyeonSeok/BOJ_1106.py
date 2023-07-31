import sys

C, N = map(int, sys.stdin.readline().split())
dp = [sys.maxsize] * (C+1)
ad = list()
dp[0] = 0
for _ in range(N):
    cost, inc = map(int, sys.stdin.readline().split())
    ad.append((cost, inc))

for i in range(C+1):
    for cost, inc in ad:
        if i+inc < C:
            dp[i+inc] = min(dp[i+inc], dp[i] + cost)    # if dp[i+inc] > 0 else dp[i] + cost
        else:
            dp[-1] = min(dp[-1], dp[i] + cost) # if dp[-1] > 0 else dp[i] + cost
print(dp[-1])