import sys

def bfs(graph, k, v):
    answer = set()
    stack = list()
    visited = [False for _ in range(len(graph))]
    visited[v] = True
    stack.append((v, sys.maxsize))
    while stack:
        node, cost = stack.pop()
        if cost < k:
            continue
        if cost >= k and cost != sys.maxsize:
            answer.add(node)
        for i, length in graph[node]:
            if visited[i]:
                continue
            visited[i] = True
            stack.append((i, min(cost, length)))
    return len(answer)

def minimize_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                continue


N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p-1].append((q-1, r))
    graph[q-1].append((p-1, r))
for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(graph, k, v-1))