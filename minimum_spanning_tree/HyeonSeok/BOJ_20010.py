N, K = map(int, input().split())
info = list()
for _ in range(K):
    a, b, cost = map(int, input().split())
    info.append((cost, (a, b)))
info.sort()
root = [i for i in range(N)]
minimum_cost = 0
inf = 1000001
graph = [[] for _ in range(N)]
# MST
for cost, nodes in info:
    a, b = nodes
    ra = root[a]
    rb = root[b]
    if ra == rb:    # 사이클인 경우
        continue
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    minimum_cost += cost
    root_node = min(ra, rb)
    for idx, node in enumerate(root):
        if node == ra or node == rb:
            root[idx] = root_node

# DFS
# 아무점이나 잡고 가장먼 끝점 찾아서 다시 그 끝점으로부터 가장먼 끝점 찾으면 트리의 지름
stack = list()
visited = [False for _ in range(N)]
visited[0] = True
stack.append((0, 0))
max_cost = 0
max_node = 0
while stack:
    node, cost = stack.pop()
    if cost >= max_cost:
        max_cost = cost
        max_node = node
    for tar, c in graph[node]:
        if visited[tar]:
            continue
        visited[tar] = True
        stack.append((tar, cost+c))
stack.append((max_node, 0))
visited = [False for _ in range(N)]
visited[max_node] = True
max_cost = 0
while stack:
    node, cost = stack.pop()
    if cost >= max_cost:
        max_cost = cost
    for tar, c in graph[node]:
        if visited[tar]:
            continue
        visited[tar] = True
        stack.append((tar, cost+c))
print(minimum_cost)
print(max_cost)