import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list()
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
dp = [0]*(K+1)
for num in num_list:
    if num <= K:
        dp[num] += 1
    for i in range(num+1, K+1):
        dp[i] += dp[i - num]
print(dp[-1])