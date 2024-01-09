# 치킨치킨치킨

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
chicken = [] # 회원들의 치킨 만족도를 리스트로 담아둠.
for i in range(N):
    chicken.append(list(map(int, sys.stdin.readline().split())))

items = [i for i in range(M)]
comb = list(combinations(items, 3)) # 시킬수 있는 치킨 조합

result = []

for i in comb: # 가능한 조합 i를
    max_value = 0
    #print(i)
    for j in range(N): # 회원마다 돌아가면서
        c1 = chicken[j][i[0]]
        c2 = chicken[j][i[1]]
        c3 = chicken[j][i[2]]
        max_value += max(c1, c2, c3) # 시킨 3가지 치킨 중 젤 높은 만족도를 저장
        #print(str(c1) + ":" + str(c2) + ":" + str(c3))
    result.append(max_value)

result.sort(reverse=True)
print(result[0])

# nCr 조합 뽑는 법 !
# from itertools import combinations
# list(combination(items, r))
