import sys

N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
answer = 0

for i in range(N):
    max_sum = 0
    for j in range(i):
        if sequence[j] < sequence[i]:
            max_sum = max(max_sum, dp[j])
    dp[i] = max_sum + sequence[i]
    answer = max(dp[i], answer)

print(answer)