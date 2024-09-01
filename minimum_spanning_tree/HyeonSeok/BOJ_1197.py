V, E = map(int, input().split())
root = [i for i in range(V)]
infos = list()
for _ in range(E):
    a, b, cost = map(int, input().split())
    infos.append((cost, a-1, b-1))
infos.sort()
answer = 0
for cost, a, b in infos:
    if root[a] == root[b]:
        continue
    answer += cost
    ra = root[a]
    rb = root[b]
    for i, node in enumerate(root):
        if node == ra or node == rb:
            root[i] = ra
print(answer)