import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = list()
start = tuple()
visited = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for j in range(n):
    for i in range(m):
        if graph[j][i] == 2:
            start = (j, i)

cost = -1
q = list()
q.append(start)
while q:
    current_q = deque(q[:])
    q.clear()
    cost += 1
    while current_q:
        y, x = current_q.popleft()
        if not visited[y][x] and graph[y][x] != 0:
            visited[y][x] = True
            graph[y][x] = cost
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= dy + y < n and 0 <= dx + x < m and not visited[y + dy][x + dx]:
                    q.append((y+dy, x+dx))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] != 0:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])