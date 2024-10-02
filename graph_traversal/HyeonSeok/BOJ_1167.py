def dfs(edges, start_node):
    stack = list()
    visited = [False for _ in range(len(edges)+1)]
    stack.append((start_node, 0))
    visited[start_node] = True
    max_dist = 0
    while stack:
        node, d = stack.pop()
        if d > max_dist:
            max_node = node
            max_dist = max(max_dist, d)
        for node, dist in edges[node]:
            if not visited[node]:
                visited[node] = True
                stack.append((node, d + dist))
    return max_node, max_dist

V = int(input())
edges = dict()
for v in range(V):
    temp = list(map(int, input().split()))
    start_node = temp[0]
    edges[start_node] = list()
    for i in range(1, len(temp)-1, 2):
        edges[start_node].append((temp[i], temp[i+1]))
max_node, max_dist = dfs(edges, start_node)
print(dfs(edges, max_node)[1])