import sys

N = int(sys.stdin.readline())
dp = [[0 for i in range(N)] for j in range(10)]
for i in range(1, 10):
    dp[i][0] = 1
for i in range(1, N):
    for num in range(10):
        if num == 0:
            dp[1][i] += dp[num][i-1]
        elif num == 9:
            dp[8][i] += dp[num][i-1]
        else:
            dp[num+1][i] += dp[num][i-1]
            dp[num-1][i] += dp[num][i-1]
answer = 0
for num in range(10):
    answer += dp[num][-1]
print(answer % 1000000000)