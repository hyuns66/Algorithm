# 카드 구매하기
# N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값

import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]

for i in range(N): # 각 카드 N개를 얻기 위해 지불해야하는 최대 금액
    for j in range(i+1):
        #print(f" i = {i}/ j = {j}")
        #print(f"array[i-j]={array[i-j]} / dp[j] = {dp[j]}")
        dp[i+1] = max(dp[i+1], array[i-j]+dp[j])
    #print(dp)

print(dp[-1])