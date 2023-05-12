# 주유소
import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))

#runOil = [sys.maxsize] * (N - 1)
minOil = oil[0]

# print(oil)
#for i in range(1, N):
#    minOil = sys.maxsize
#    for j in range(i):
#        if oil[j] < minOil:
#            minOil = oil[j]
#    runOil[i - 1] = minOil

# print(runOil)

cost = 0
for i in range(len(road)):
    if oil[i] < minOil:
        minOil = oil[i]
    cost += road[i] * minOil

print(cost)

# 첫시도 -> 2중 for문이라 O(N^2)이 돼어 시간 초과 41점
# 위의 문제점을 고쳐 2차시도 100점 