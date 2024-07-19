# 쉬운 계단 수
# 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
# 길이가 N인 계단 수는 총 몇개?

import sys

# 1<=n<=100

n = int(sys.stdin.readline())
dp = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for len in range(2, n + 1):
    dp[len][0] = dp[len - 1][1]  # 0
    dp[len][9] = dp[len - 1][8]  # 9
    for num in range(1, 9):  # 1~8
        dp[len][num] = (dp[len - 1][num - 1] + dp[len - 1][num + 1]) % 1000000000

print(sum(dp[n]) % 1000000000)
