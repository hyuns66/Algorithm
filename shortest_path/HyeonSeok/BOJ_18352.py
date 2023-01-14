import sys
from heapq import *

N, M, K, X = map(int, sys.stdin.readline().split())
inf = sys.maxsize
town = [list() for i in range(N+1)]
answer = list()

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    town[a].append((b, 1))

q = list()
heappush(q, (X, 0))
distance = [inf] * (N+1)
distance[X] = 0
while q:
    node, dist = heappop(q)     # dist : X로부터 node까지의 거리
    if distance[node] < dist:    # 이미 더 가까운 루트가 있으면 pass
        continue
    for destination in town[node]:  # 이 노드와 연결된 모든 노드에 대해서
        cost = dist + destination[1]
        if cost < distance[destination[0]]:
            distance[destination[0]] = cost
            # town[X][destination] = cost
            heappush(q, (destination[0], cost))

flag = True
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        flag = False

if flag:
    print(-1)

