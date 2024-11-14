n = int(input())
dp = [[0, 0] for _ in range(n)]
squares = list()
for i in range(n):
    a, b = map(int, input().split())
    squares.append((a, b))
dp[0][0] = squares[0][0]
dp[0][1] = squares[0][1]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + squares[i][0] + abs(squares[i][1] - squares[i-1][1]), 
                   dp[i-1][1] + squares[i][0] + abs(squares[i][1] - squares[i-1][0]))
    dp[i][1] = max(dp[i-1][0] + squares[i][1] + abs(squares[i][0] - squares[i-1][1]),
                   dp[i-1][1] + squares[i][1] + abs(squares[i][0] - squares[i-1][0]))
print(max(dp[-1][0], dp[-1][1]))