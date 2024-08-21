def check(elected):
    if False in elected:
        return False
    return True

N, M, K = map(int, input().split())
city = [i for i in range(N)]
elected = [False for _ in range(N)]
elects = set(map(int, input().split()))
for e in elects:
    elected[e-1] = True
info = list()
for _ in range(M):
    u, v, cost = map(int, input().split())
    info.append((cost, (u, v)))
info.sort()
root = [i for i in range(N)]
answer = 0
for cost, nodes in info:
    u = nodes[0]-1
    v = nodes[1]-1
    if elected[u] and elected[v]:
        continue
    if root[u] == root[v]:
        continue
    root_num = min(u, v)
    a = root[u]
    b = root[v]
    is_elected = elected[u] or elected[v]
    for i in range(N):
        if root[i] == a or root[i] == b:
            root[i] = root_num
            elected[i] = is_elected
    answer += cost
    if check(elected):
        break
print(answer)