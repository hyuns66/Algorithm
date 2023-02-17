import sys

num = int(sys.stdin.readline())
stair = list()
answer = 0

for _ in range(num):
    stair.append(int(sys.stdin.readline()))

dp = [0] * num

for position in range(num):
    if position == 0:
        dp[position] = stair[0]
    elif position == 1:
        dp[position] = stair[0] + stair[1]
    elif position == 2:
        dp[position] = max(stair[0] + stair[2], stair[1] + stair[2])
    else:
        dp[position] = max(dp[position - 3] + stair[position - 1] + stair[position], dp[position - 2] + stair[position])

print(dp[-1])