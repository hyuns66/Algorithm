N, M = map(int, input().split())
sex = list(input().split())
info = list()
for _ in range(M):
    u, v, cost = map(int, input().split())
    info.append((cost, (u-1, v-1)))
info.sort()
root = [i for i in range(N)]
answer = 0
for cost, nodes in info:
    u, v = nodes
    if sex[u] == sex[v]:
        continue
    if root[u] == root[v]:
        continue
    root_node = min(root[u], root[v])
    u = root[u]
    v = root[v]
    for idx, node in enumerate(root):
        if node == u or node == v:
            root[idx] = root_node
    answer += cost
print(answer)