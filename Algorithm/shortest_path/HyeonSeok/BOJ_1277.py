import heapq
import sys
import math

def dijkstra(start):
    distance = [inf] * (N+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for d, n in graph[now]:
            cost = dist + d
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(heap, (cost, n))
    return distance

N, W = map(int, sys.stdin.readline().split())
M = float(sys.stdin.readline())
inf = sys.maxsize

tower_xy = [1 for i in range(N+1)]
graph = [list() for k in range(N+1)]
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    tower_xy[i+1] = (x + 10000, y + 10000)

for g in range(1, N+1):
    for i in range(1, N+1):
        dist = math.sqrt(((tower_xy[g][0] - tower_xy[i][0]) ** 2) + ((tower_xy[g][1] - tower_xy[i][1]) ** 2))
        if dist > M:
            continue
        graph[g].append((dist, i))

for i in range(W):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((0, b))
    graph[b].append((0, a))

answer = dijkstra(1)

print(int(1000*answer[N]))