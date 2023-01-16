import copy
import sys

N = int(sys.stdin.readline())
inf = sys.maxsize
time_stamp = [list() for i in range(N)]
graph = [list() for j in range(N)]

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    time_stamp[i] = copy.deepcopy(temp)
    graph[i] = copy.deepcopy(temp)


for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or i == k:
                continue
            if graph[j][k] >= graph[j][i] + graph[i][k]:
                graph[j][k] = inf
                graph[k][j] = inf
                if time_stamp[j][k] > graph[j][i] + graph[i][k]:
                    print(-1)
                    exit()


answer = 0
for t in graph:
    for num in t:
        if num != inf:
            answer += num

print(answer >> 1)