import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [False] * N
dp[0] = True
for i in range(N):
    if not dp[i]:
        continue
    for dist in range(1, K+1):
        if i + dist < N and dist * (1 + abs(num_list[i] - num_list[i + dist])) <= K:
            dp[i + dist] = True
print('YES' if dp[-1] else 'NO')
