import sys

N, M = map(int, sys.stdin.readline().split())
graph = list()
prompt = list()
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
for i in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    prompt.append(temp)
for y in range(N):
    for x in range(N):
        top = graph[y - 1][x] if y > 0 else 0
        left = graph[y][x - 1] if x > 0 else 0
        cross = graph[y - 1][x - 1] if y > 0 and x > 0 else 0
        graph[y][x] = graph[y][x]+left+top-cross
for p in prompt:
    x1, y1 = p[1]-1, p[0]-1
    x2, y2 = p[3]-1, p[2]-1
    top = graph[y1 - 1][x2] if y1 > 0 else 0
    left = graph[y2][x1 - 1] if x1 > 0 else 0
    cross = graph[y1 - 1][x1 - 1] if y1 > 0 and x1 > 0 else 0
    print(graph[y2][x2]-left-top+cross)
