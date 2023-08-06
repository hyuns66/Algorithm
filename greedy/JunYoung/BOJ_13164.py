# 행복 유치원

import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())

heights = list(map(int, sys.stdin.readline().split()))

# <시도1>

#groupIndex = [i for i in range(1, N)]
#cresult = list(combinations(groupIndex, K - 1))  # K개의 그룹으로 나누려면 K-1개의 구분선만 뽑으면 됨.
#mincost = sys.maxsize
#for choice in cresult:
#    cost = 0
#    short = heights[0]
#    for i in choice:
#        cost += heights[i - 1] - short
#        if cost >= mincost:
#            break
#        short = heights[i]
#    cost += heights[-1] - short
#    #print(cost)
#    if cost < mincost:
#        mincost = cost
#print(mincost)

# 메모리 초과 - cresult에서 모든 조합을 계산해서 그런 것 같긴한데..

# <시도 2>
diff = []
for i in range(1, len(heights)):
    diff.append(heights[i]-heights[i-1])

# K개의 그룹 => K-1개의 경계를 제외할 수 있다.
diff.sort(reverse=True)
#print(diff)

cost = 0
for i in range(K-1, len(diff)):
    cost += diff[i]
print(cost)

# for i in range(K-1, ): 하면 K-1부터 끝까지 일 줄 알았는데 아니고, 반복횟수 K-1번으로 인식된다.

# 배운 점: 단위를 확인하며 brute_force가 가능하지 않음을 짐작할 수 있어야겠다.
