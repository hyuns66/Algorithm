"""
Dijkstra 풀이
"""

import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001

heap = []
heapq.heappush(heap, (0, N))
while heap:
    time, now = heapq.heappop(heap)
    if now > 100000:
        continue
    visited[now] = True
    if now == K:
        print(time)
        break
    temp = now << 1
    if temp <= 100000 and not visited[now << 1]:
        heapq.heappush(heap, (time, now << 1))
    if now + 1 <= 100000 and not visited[now + 1]:
        heapq.heappush(heap, (time + 1, now + 1))
    if now - 1 >= 0 and not visited[now - 1]:
        heapq.heappush(heap, (time + 1, now - 1))

"""
0-1 BFS 풀이
"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001

d = deque()
d.appendleft((0, N))

while d:
    time, now = d.popleft()
    visited[now] = True
    if now == K:
        print(time)
        break
    if (now << 1) <= 100000 and not visited[now << 1]:
        d.appendleft((time, now << 1))
    if now + 1 <= 100000 and not visited[now + 1]:
        d.append((time + 1, now + 1))
    if now - 1 >= 0 and not visited[now - 1]:
        d.append((time + 1, now - 1))