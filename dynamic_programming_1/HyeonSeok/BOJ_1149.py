import sys

N = int(input ())
rgb = list()
for _ in range(N):
    rgb.append(list(map(int, input().split())))
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]
for i in range(1, N):   # 집 인덱스
    for j in range(3):  # 해당 인덱스에 칠해야할 색
        cost = sys.maxsize
        for k in range(3):  # 인접한 이전 집 비용 계산
            if j == k:
                continue
            cost = min(dp[i-1][k] + rgb[i][j], cost)
        dp[i][j] = cost
print(min(dp[-1]))