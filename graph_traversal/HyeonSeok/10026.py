import sys

def dfs(graph, x, y, visited, node):
    visited[y][x] = True
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            py, px = (y+dy, x+dx)
            if py < 0 or px < 0 or py >= len(graph) or px >= len(graph[0]):
                continue
            if visited[py][px]:
                continue
            if graph[py][px] not in node:
                continue
            stack.append((py, px))
            visited[py][px] = True
    return 1

N = int(input())
graph = list()
visited_1 = [[False for _ in range(N)] for _ in range(N)]
visited_2 = [[False for _ in range(N)] for _ in range(N)]
answer = [0, 0]
for _ in range(N):
    graph.append(list(input()))
for y in range(N):
    for x in range(N):
        if not visited_1[y][x]:
            answer[0] += dfs(graph, x, y, visited_1, [graph[y][x]])
        if not visited_2[y][x]:
            if graph[y][x] == 'B':
                node = ['B']
            else:
                node = ['R', 'G']
            answer[1] += dfs(graph, x, y, visited_2, node)
print(*answer)