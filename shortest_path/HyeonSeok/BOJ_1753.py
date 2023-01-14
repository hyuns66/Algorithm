import heapq
import sys

# def dijkstra(start):
#     global distance
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (start, 0))
#     while q:
#         now, dist = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for dest in graph[now]:
#             cost = dist + dest[1]
#             if cost < distance[dest[0]]:
#                 distance[dest[0]] = cost
#                 heapq.heappush(q, (dest[0], cost))

# def dijkstra(start):
#     #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
#     global distance
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (start, 0))
#
#     #힙에 원소가 없을 때 까지 반복.
#     while q:
#         now, dist = heapq.heappop(q)
#
#         #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
#         if distance[now] < dist:
#             continue
#
#         for next_node, w in graph[now]:
#             #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
#             # = 다음 노드까지의 가중치(next_wei)
#             cost = w + dist
#             #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
#             if cost < distance[next_node]:
#                 #계산했던 next_wei를 가중치 테이블에 업데이트.
#                 distance[next_node] = cost
#                 #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
#                 heapq.heappush(q,(next_node, cost))

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
# for i in range(V):
#     d = distance[i+1]
#     if d == inf:
#         print("INF")
#     else:
#         print(d)

# import sys
# import heapq
#
# input = sys.stdin.readline
# inf = sys.maxsize
# V, E = map(int, input().split())
# #시작점 K
# K = int(input())
# #가중치 테이블 dp
# distance = [inf]*(V+1)
# q = []
# graph = [[] for _ in range(V + 1)]
#
# def Dijkstra(start):
#     #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
#     distance[start] = 0
#     heapq.heappush(q,(start, 0))
#
#     #힙에 원소가 없을 때 까지 반복.
#     while q:
#         now, wei = heapq.heappop(q)
#
#         #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
#         if distance[now] < wei:
#             continue
#
#         for next_node, w in graph[now]:
#             #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
#             # = 다음 노드까지의 가중치(next_wei)
#             next_wei = w + wei
#             #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
#             if next_wei < distance[next_node]:
#                 #계산했던 next_wei를 가중치 테이블에 업데이트.
#                 distance[next_node] = next_wei
#                 #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
#                 heapq.heappush(q,(next_node,next_wei))
#
# #초기화
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     #(가중치, 목적지 노드) 형태로 저장
#     graph[u].append((v, w))
#
#
# Dijkstra(K)
# for i in range(1,V+1):
#     print("INF" if distance[i] == inf else distance[i])