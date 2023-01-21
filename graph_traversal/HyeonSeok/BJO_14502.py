import copy
import sys
from collections import deque


def BFS(wall_set: list):
    global virus, v_start
    g = [grgr[:] for grgr in graph]
    while wall_set:
        w = wall_set.pop()
        g[w[0]][w[1]] = 1
    v_area = 0
    for v in virus:
        g[v[0]][v[1]] = 0
        q = deque()
        q.append((v[0], v[1]))
        while q:
            y, x = q.popleft()
            if g[y][x] == 0:
                g[y][x] = 2
                v_area += 1
                for dy, dx in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                    if 0 <= y + dy < N and 0 <= x + dx < M and g[y + dy][x + dx] == 0:
                        q.append((y + dy, x + dx))
    # for i in range(N):
    #     print(*g[i])
    return v_area


N, M = map(int, sys.stdin.readline().split())
graph = list()
walls = list()
virus = list()
wall_cnt = 3

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 벽을 세울 수 있는 좌표셋 3쌍의 경우의 수 생성
for i in range(N * M):
    if graph[int(i / M)][i % M] == 1:
        wall_cnt += 1
        continue
    elif graph[int(i / M)][i % M] == 2:
        virus.append((int(i / M), i % M))
        continue
    for j in range(i + 1, N * M):
        if graph[int(j / M)][j % M] != 0:
            continue
        for k in range(j + 1, N * M):
            if graph[int(k / M)][k % M] != 0:
                continue
            else:
                walls.append([(int(i / M), i % M), (int(j / M), j % M), (int(k / M), k % M)])

answer = 0

# BFS 함수에 인자로 전달, 실행
while walls:
    v_cnt = BFS(walls.pop())
    temp = N * M - v_cnt - wall_cnt
    if answer < temp:
        answer = temp

print(answer)
