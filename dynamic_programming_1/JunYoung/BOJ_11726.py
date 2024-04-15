# 2xn 타일링
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
# 2x1 타일은 사실 2xn 을 채울때 2x1, 2x1 => 2x2로 밖에 못채우니까 2x2와 동급!
# n을 1,2로 어떻게 구성할지가 관건!
# Fn = Fn-1 + Fn-2

import sys

n = int(sys.stdin.readline())

memo = [0 for _ in range(max(3, n + 1))]  # index: 0~n (n+1개 생성)
memo[1] = 1
memo[2] = 2 # 그냥 range(n+1)로 했더니 n=1일땐 memo[2]에 입력할 수 x

for i in range(3, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 10007

print(memo[n])
