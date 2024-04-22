# 2xn 타일링 2
# 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

import sys
n = int(sys.stdin.readline())

# n을 2와 1로 나눌 수 있다.

dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 3

# F(n) = F(n-1) + F(n-2) * 3
# 2개를 추가하는 경우의 수가 1x2, 2x2, 1x1 세 경우가 인줄 알았는데
# 1x1은 1을 추가하는걸로 쳐야한다.

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[n])