def count(idx, dp, x):
    if idx == -1:
        return x
    elif idx == 0:
        return 1
    elif x == 1:
        return 0
    elif dp[idx-1][1]+2 == x:
        return dp[idx-1][0]+1
    elif dp[idx-1][1]+2 > x:
        return count(idx-1, dp, x-1)
    elif x < dp[idx-1][1]*2+3:
        return dp[idx-1][0]+1+count(idx-1, dp, x-dp[idx-1][1]-2)
    else:
        return dp[idx][0]

N, X = map(int, input().split())
dp = [(1, 1)]
for i in range(1, N+1):
    dp.append((dp[i-1][0]*2+1, dp[i-1][1]*2+3))
print(count(len(dp)-1, dp, X))