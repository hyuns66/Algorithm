import sys
from collections import deque

def bfs(y, x):
    global graph, N, L, R, visited, union_list
    q = deque()
    q.append((y, x))
    union = [graph[y][x], 1, [(y, x)]]
    visited[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        for dir_y, dir_x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            tar_y, tar_x = cur_y + dir_y, cur_x + dir_x
            if tar_y < 0 or tar_y >= N or tar_x < 0 or tar_x >= N:
                continue
            if not visited[tar_y][tar_x] and L <= abs(graph[cur_y][cur_x] - graph[tar_y][tar_x]) <= R:
                union[0] += graph[tar_y][tar_x]
                union[1] += 1
                union[2].append((tar_y, tar_x))
                visited[tar_y][tar_x] = True
                q.append((tar_y, tar_x))
    if len(union[2]) > 1:
        union_list.append(union)

def swap():
    global N, L, R, graph, visited, union_list
    union_list = list()
    visited = [[False for i in range(N)] for j in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(y, x)
    if not union_list:
        return False
    for union in union_list:
        union_value = union[0] // union[1]
        for y, x in union[2]:
            graph[y][x] = union_value
    return True

N, L, R = map(int, sys.stdin.readline().split())
graph = list()
visited = [[False for i in range(N)] for j in range(N)]
union_list = list()

for y in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0
while True:
    flag = swap()
    if not flag:
        break
    else:
        answer += 1
print(answer)