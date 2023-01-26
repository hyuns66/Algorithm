import sys

N, M = map(int, sys.stdin.readline().split())
inf = sys.maxsize
graph = [[inf for i in range(N)] for j in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j == k:
                graph[i][i] = 0
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

cv = sys.maxsize
answer = -1
for i in range(N):
    temp = 0
    for j in range(N):
        temp += graph[i][j]
    if temp < cv:
        answer = i + 1
        cv = temp

print(answer)