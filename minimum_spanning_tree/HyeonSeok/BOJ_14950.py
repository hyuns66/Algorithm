N, M, t = map(int, input().split())
info = list()
for _ in range(M):
    a, b, cost = map(int, input().split())
    info.append((cost, (a, b)))
info.sort()
answer = 0
count = 0
root = [i for i in range(N)]
for cost, nodes in info:
    a = nodes[0]-1
    b = nodes[1]-1
    if root[a] == root[b]:
        continue
    answer += cost
    answer += count*t
    count += 1
    j = root[a]
    k = root[b]
    root_node = min(j, k)
    for num, node in enumerate(root):
        if node == j or node == k:
            root[num] = root_node
print(answer)