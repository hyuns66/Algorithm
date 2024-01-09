import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
inf = sys.maxsize
distance = [inf] * (V + 1)

graph = [[] for i in range(V+1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))

# dijkstra(K)

distance = [inf] * (V+1)
distance[K] = 0
q = []
heapq.heappush(q, (0, K))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for dest in graph[now]:
        cost = dist + dest[0]
        if cost < distance[dest[1]]:
            distance[dest[1]] = cost
            heapq.heappush(q, (cost, dest[1]))

for i in range(1, V+1):
    print("INF" if distance[i] == inf else distance[i])
