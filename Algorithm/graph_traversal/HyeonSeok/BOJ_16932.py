import sys
from collections import deque


def BFS(node, is_changed, v):
    global graph
    # for a in range(N):
    #     visited[a] = [False] * M
    v[node[0]][node[1]] = True
    q = deque()
    q.append((node[0], node[1], is_changed))
    total = 1
    added_total = 0
    while q:
        y, x, is_changed = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            cur_x = x + dx
            cur_y = y + dy
            if 0 > cur_y or cur_y >= N or 0 > cur_x or cur_x >= M:
                continue
            if graph[cur_y][cur_x] == 1 and not v[cur_y][cur_x]:
                q.append((cur_y, cur_x, is_changed))
                v[cur_y][cur_x] = True
                graph[cur_y][cur_x] = num
                total += 1
            # elif graph[cur_y][cur_x] == 0 and not is_changed:
            #     change_list.append((cur_y, cur_x))
    # while change_list:
    #     cur_y, cur_x = change_list.pop()
    #     added_temp = BFS((cur_y, cur_x), True, [vv[:] for vv in v])
    #     if added_temp > added_total:
    #         added_total = added_temp
    return total + added_total


N, M = map(int, sys.stdin.readline().split())
graph = list()
visited = list()
group = list()
num = 0

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([False] * M)

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            num += 1
            graph[i][j] = num
            group.append(BFS((i, j), False, visited))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            temp = 0
            s = set()
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                cur_x = j + dx
                cur_y = i + dy
                if 0 > cur_y or cur_y >= N or 0 > cur_x or cur_x >= M:
                    continue
                if graph[cur_y][cur_x] != 0:
                    s.add(graph[cur_y][cur_x] - 1)
            while s:
                temp += group[s.pop()]
            answer = max(answer, temp + 1)
print(answer)
