import sys

V, E = map(int, sys.stdin.readline().split())
inf = sys.maxsize
graph = [[inf for j in range(V)] for i in range(V)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = c

for i in range(V):
    for j in range(V):
        for k in range(V):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

answer = sys.maxsize
for i in range(V):
    if answer > graph[i][i]:
        answer = graph[i][i]

print(-1 if answer == sys.maxsize else answer)