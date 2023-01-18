import sys
from collections import deque

def append_node(node, visited, route):
    visited[node] = True
    route.append(node + 1)
    for n in graph[node]:
        if not visited[n]:
            append_node(n, visited, route)
    return route

def DFS_recursive(start):
    visited = [False] * N
    route = list()
    append_node(start, visited, route)
    return route

def DFS_stack(start):
    visited = [False] * N
    route = list()
    stack = list()
    stack.append(start)
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            route.append(now + 1)
            for node in graph[now]:
                stack.append(node)
    return route

def BFS(start):
    visited = [False] * N
    q = deque()
    q.append(start)
    route = list()
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        route.append(now + 1)
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
    return route

N, M, V = map(int, sys.stdin.readline().split())
graph = [list() for i in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for g in graph:
    g.sort(reverse=False)

bfs = BFS(V - 1)
# dfs = DFS_recursive(V - 1)

for g in graph:
    g.sort(reverse=True)

dfs = DFS_stack(V - 1)

print(*dfs)
print(*bfs)