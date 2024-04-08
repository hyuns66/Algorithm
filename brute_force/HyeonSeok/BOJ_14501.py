N = int(input())
schedule = list()
for _ in range(N):
    schedule.append(list(map(int, input().split())))
    
dp = [0 for _ in range(N+1)]
for idx in range(len(schedule)+1):
    for i in range(idx):
        T, P = schedule[i]
        if T == idx-i:
            dp[idx] = max(dp[idx], dp[i] + P)
    if idx != 0:
        dp[idx] = max(dp[idx], dp[idx-1])
print(dp[-1])