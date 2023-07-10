import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

chicken_addr = list()
house_addr = list()
graph = list()

for y in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

# 치킨집이랑 집 주소 리스트만들기
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            house_addr.append((y, x))
        elif graph[y][x] == 2:
            chicken_addr.append([list(), (y, x)])

for i, chicken in enumerate(chicken_addr):
    y, x = chicken[1]
    for house in house_addr:
        y_h, x_h = house
        dist = abs(y-y_h) + abs(x-x_h)
        chicken_addr[i][0].append(dist)

answer = sys.maxsize
chicken_max = itertools.combinations(chicken_addr, M)
for cm in chicken_max:
    min_dist = [sys.maxsize]*len(house_addr)
    for c in cm:
        min_dist = [min(dist1, dist2) for dist1, dist2 in zip(c[0], min_dist)]
    answer = min(answer, sum(min_dist))

print(answer)