def dfs(y, x, visited, graph):
    stack = list()
    stack.append((y, x))
    visited[y][x] = True
    count = 1
    while stack:
        y, x = stack.pop()
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            py, px = (y+dy, x+dx)
            if py < 0 or py >= len(graph) or px < 0 or px >= len(graph):
                continue
            if not visited[py][px] and graph[py][px] == '1':
                visited[py][px] = True
                stack.append((py, px))
                count += 1
    return count


N = int(input())
graph = list()
for _ in range(N):
    graph.append(list(input()))
visited = [[False for _ in range(N)] for _ in range(N)]
counts = list()
for y in range(N):
    for x in range(N):
        if graph[y][x] == '1' and not visited[y][x]:
            counts.append(dfs(y, x, visited, graph))

counts.sort()
print(len(counts))
for c in counts:
    print(c)