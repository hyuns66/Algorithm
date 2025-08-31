import sys

n = int(input())
m = int(input())
graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a][b], c)
for z in range(n):
    for y in range(n):
        for x in range(n):
            if z == y or z == x or y == x:
                continue
            graph[y][x] = min(graph[y][x], graph[y][z] + graph[z][x])
for y in range(n):
    for x in range(n):
        if graph[y][x] == sys.maxsize:
            graph[y][x] = 0
for g in graph:
    print(*g)