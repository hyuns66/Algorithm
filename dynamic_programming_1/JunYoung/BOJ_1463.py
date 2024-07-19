# 1로 만들기
import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(max(4, (N + 1)))]

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    min_cal = sys.maxsize
    if i % 2 == 0:
        min_cal = min(dp[i // 2] + 1, min_cal)
    if i % 3 == 0:
        min_cal = min(dp[i // 3] + 1, min_cal)
    min_cal = min(dp[i - 1] + 1, min_cal)
    dp[i] = min_cal  # dp 값 기록!

print(dp[N])
