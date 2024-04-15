# 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        #print("i="+str(i)+"j="+str(j))
        if arr[j]<arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

#dp로 풀면 O(N^2) -> 이분 탐색 O(NlogN)
#https://velog.io/@black_han26/%EB%B0%B1%EC%A4%80Python-11053-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-LIS