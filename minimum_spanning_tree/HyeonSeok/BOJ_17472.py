from collections import deque

def cluster(y, x, graph, node_num, visited):
    visited[y][x] = True
    queue = deque()
    queue.append((y, x))
    graph[y][x] = node_num
    while queue:
        py, px = queue.popleft()
        for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            desty = py + dy
            destx = px + dx
            if desty < 0 or desty >= len(graph) or destx < 0 or destx >= len(graph[0]):
                continue
            if graph[desty][destx] == 0:
                continue
            if not visited[desty][destx]:
                graph[desty][destx] = node_num
                visited[desty][destx] = True
                queue.append((desty, destx))
            
def scan(y, x, graph, bridges):
    for dir in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        dy = y + dir[0]
        dx = x + dir[1]
        length = 1
        while dy >= 0 and dx >= 0 and dy < len(graph) and dx < len(graph[0]):
            if graph[dy][dx] == graph[y][x]:
                break
            if graph[dy][dx] != 0:
                if length >= 3:
                    bridges[graph[y][x]][graph[dy][dx]] = min(bridges[graph[y][x]][graph[dy][dx]], length-1)
                break
            length += 1
            dy += dir[0]
            dx += dir[1]

N, M = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))

node_num = 1
visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0 or visited[y][x]:
            continue
        cluster(y, x, graph, node_num, visited)
        node_num += 1
bridges = [[11 for _ in range(node_num+1)] for _ in range(node_num+1)]
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            continue
        scan(y, x, graph, bridges)

union = [i for i in range(node_num)]
costs = list()
for i in range(node_num):
    for j in range(i, node_num):
        if bridges[i][j] == 11:
            continue
        costs.append((bridges[i][j], (i, j)))
costs.sort()
answer = 0

for cost, nodes in costs:
    a, b = nodes
    if union[a] == union[b]:
        continue
    root_node = min(union[a], union[b])
    j = union[a]
    k = union[b]
    for i, num in enumerate(union):
        if num == j or num == k:
            union[i] = root_node
    answer += cost

cache = union[1]
for i in range(2, len(union)):
    if i == 0:
        continue
    if cache != union[i]:
        answer = -1
print(answer)
