import sys
n = int(sys.stdin.readline())
dp = [0]*n
for i in range(n):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + (2 * dp[i-2])
print(dp[-1] % 10007)