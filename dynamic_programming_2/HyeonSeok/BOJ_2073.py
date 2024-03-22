import sys

def update_dp(dp, l, c, max_length):
    for idx in range(max_length, 0, -1):
        value = dp[idx]
        if idx - l < 0:
            continue
        if dp[idx-l] >= 0:
            temp = min(c, dp[idx-l])
            dp[idx] = max(temp, value)
        
D, P = map(int, sys.stdin.readline().split())
dp = [-1 for _ in range(D+1)]
dp[0] = sys.maxsize
for _ in range(P):
    L, C = map(int, sys.stdin.readline().split())
    update_dp(dp, L, C, D)
    
print(dp[-1])