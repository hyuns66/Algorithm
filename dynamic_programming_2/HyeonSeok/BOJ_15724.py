import sys

N, M = map(int, sys.stdin.readline().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
for y in range(N):
    for x in range(M):
        top = graph[y-1][x] if y > 0 else 0
        left = graph[y][x-1] if x > 0 else 0
        cross = graph[y-1][x-1] if (y > 0 and x > 0) else 0
        graph[y][x] += (top + left - cross)
K = int(sys.stdin.readline())
answer = list()
for _ in range(K):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    top = graph[y2 - 1][x1 - 2] if x1 > 1 else 0
    left = graph[y1 - 2][x2 - 1] if y1 > 1 else 0
    cross = graph[y1 - 2][x1 - 2] if (y1 > 1 and x1 > 1) else 0
    answer.append(graph[y2 - 1][x2 - 1] - top - left + cross)
for a in answer:
    print(a)